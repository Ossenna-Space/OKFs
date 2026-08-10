#!/usr/bin/env python3
"""Deterministic acquisition, transformation, hydration, and retention for OKF sources."""

from __future__ import annotations

import argparse
import copy
import fnmatch
import hashlib
import html
from html.parser import HTMLParser
import json
import mimetypes
import os
from pathlib import Path, PurePosixPath
import random
import re
import shutil
import sys
import tempfile
from datetime import datetime, timezone
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.parse import quote, urlparse
from urllib.request import Request, urlopen


SCHEMA_VERSION = 1
TOOL_VERSION = "0.1.0"
USER_AGENT = f"okf-source-manager/{TOOL_VERSION}"
LIFECYCLE_ACTIVE = "active"
LIFECYCLE_SUSPECTED = "suspected-unavailable"
LIFECYCLE_ARCHIVED = "archived-unavailable"
STORAGE_MODES = {"reference-only", "vendored"}
TRANSFORM_VERSIONS = {
    "markdown-copy": 1,
    "text-to-markdown": 1,
    "html-to-markdown": 1,
}


class SourceError(RuntimeError):
    """A safe, user-facing source-management error."""


def now_utc() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def canonical_json(value: Any) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def read_json(path: Path) -> dict[str, Any]:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise SourceError(f"required JSON file not found: {path}") from exc
    except json.JSONDecodeError as exc:
        raise SourceError(f"invalid JSON in {path}: {exc}") from exc
    if not isinstance(value, dict):
        raise SourceError(f"JSON root must be an object: {path}")
    return value


def atomic_write_json(path: Path, value: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    payload = json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    handle = tempfile.NamedTemporaryFile(
        mode="w", encoding="utf-8", newline="\n", delete=False, dir=path.parent, prefix=f".{path.name}.", suffix=".tmp"
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            handle.write(payload)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def safe_component(value: str) -> str:
    result = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-.")
    if not result or result in {".", ".."}:
        raise SourceError(f"unsafe empty path component derived from {value!r}")
    return result


def safe_logical_path(value: str) -> PurePosixPath:
    path = PurePosixPath(value)
    if path.is_absolute() or not path.parts or any(part in {"", ".", ".."} for part in path.parts):
        raise SourceError(f"unsafe logical path: {value!r}")
    return path


def project_relative(project: Path, path: Path) -> str:
    return path.resolve().relative_to(project.resolve()).as_posix()


def resolve_project_path(project: Path, relative: str) -> Path:
    rel = safe_logical_path(relative)
    result = (project / Path(*rel.parts)).resolve()
    try:
        result.relative_to(project.resolve())
    except ValueError as exc:
        raise SourceError(f"path escapes project: {relative}") from exc
    return result


def source_paths(project: Path, source_id: str) -> tuple[Path, Path, Path]:
    safe_component(source_id)
    source_dir = project / "okf" / "sources"
    return source_dir / "source.json", source_dir / "source.lock.json", project / "okf" / "raw"


def validate_manifest(manifest: dict[str, Any], source_id: str) -> None:
    if manifest.get("schema_version") != SCHEMA_VERSION:
        raise SourceError(f"unsupported source schema_version: {manifest.get('schema_version')!r}")
    if manifest.get("id") != source_id:
        raise SourceError(f"manifest id {manifest.get('id')!r} does not match source {source_id!r}")
    storage = manifest.get("storage", {})
    if not isinstance(storage, dict):
        raise SourceError("storage must be an object")
    for kind in ("originals", "normalized"):
        mode = storage.get(kind, "reference-only")
        if mode not in STORAGE_MODES:
            raise SourceError(f"storage.{kind} must be one of {sorted(STORAGE_MODES)}")
    items = manifest.get("items")
    if not isinstance(items, list) or not items:
        raise SourceError("items must be a non-empty array")
    seen: set[str] = set()
    for item in items:
        if not isinstance(item, dict):
            raise SourceError("each source item must be an object")
        item_id = str(item.get("id", ""))
        safe_component(item_id)
        if item_id in seen:
            raise SourceError(f"duplicate source item id: {item_id}")
        seen.add(item_id)
        fetch = item.get("fetch")
        if not isinstance(fetch, dict) or fetch.get("adapter") not in {"github-tree", "https", "local-file"}:
            raise SourceError(f"item {item_id}: unsupported or missing fetch adapter")
        if "credential" in fetch or "token" in fetch or "password" in fetch:
            raise SourceError(f"item {item_id}: store only credential_ref, never credential values")
        transforms = item.get("transform")
        if not isinstance(transforms, list) or not transforms:
            raise SourceError(f"item {item_id}: transform must be a non-empty array")
        for step in transforms:
            if not isinstance(step, dict):
                raise SourceError(f"item {item_id}: transform step must be an object")
            name = step.get("name")
            if name not in TRANSFORM_VERSIONS:
                raise SourceError(f"item {item_id}: unknown transform {name!r}")
            if step.get("version") != TRANSFORM_VERSIONS[name]:
                raise SourceError(
                    f"item {item_id}: transform {name!r} requires version {TRANSFORM_VERSIONS[name]}"
                )


def request_bytes(url: str, *, accept: str | None = None) -> tuple[bytes, dict[str, Any]]:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        raise SourceError(f"network URL must use HTTP(S): {url}")
    headers = {"User-Agent": USER_AGENT}
    if accept:
        headers["Accept"] = accept
    try:
        with urlopen(Request(url, headers=headers), timeout=30) as response:
            data = response.read()
            return data, {
                "resolved_url": response.geturl(),
                "media_type": response.headers.get_content_type(),
                "etag": response.headers.get("ETag"),
                "last_modified": response.headers.get("Last-Modified"),
            }
    except HTTPError as exc:
        raise SourceError(f"HTTP {exc.code} retrieving {url}") from exc
    except URLError as exc:
        raise SourceError(f"failed to retrieve {url}: {exc.reason}") from exc


def request_json(url: str) -> dict[str, Any]:
    data, _ = request_bytes(url, accept="application/vnd.github+json")
    try:
        value = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise SourceError(f"invalid JSON response from {url}") from exc
    if not isinstance(value, dict):
        raise SourceError(f"expected an object response from {url}")
    return value


def pattern_matches(path: str, patterns: list[str]) -> bool:
    for pattern in patterns:
        if fnmatch.fnmatchcase(path, pattern):
            return True
        if pattern.startswith("**/") and fnmatch.fnmatchcase(path, pattern[3:]):
            return True
    return False


def deterministic_selection(candidates: list[dict[str, Any]], selection: Any) -> list[dict[str, Any]]:
    ordered = sorted(candidates, key=lambda entry: entry["source_path"])
    if selection is None:
        return ordered
    if not isinstance(selection, dict) or selection.get("strategy") != "random":
        raise SourceError("selection must use the supported 'random' strategy")
    count = selection.get("count")
    seed = selection.get("seed")
    if not isinstance(count, int) or count < 1:
        raise SourceError("random selection count must be a positive integer")
    if not isinstance(seed, int):
        raise SourceError("random selection seed must be an integer")
    if count > len(ordered):
        raise SourceError(f"cannot select {count} documents from {len(ordered)} candidates")
    indices = sorted(random.Random(seed).sample(range(len(ordered)), count))
    return [ordered[index] for index in indices]


def discover_github_tree(item: dict[str, Any]) -> list[dict[str, Any]]:
    fetch = item["fetch"]
    repository = str(fetch.get("repository", ""))
    parts = repository.split("/")
    if len(parts) != 2 or not all(parts):
        raise SourceError(f"item {item['id']}: repository must be OWNER/REPO")
    ref = str(fetch.get("ref", "main"))
    root = str(fetch.get("path", "")).strip("/")
    includes = fetch.get("include", ["**/*"])
    if not isinstance(includes, list) or not all(isinstance(value, str) for value in includes):
        raise SourceError(f"item {item['id']}: include must be an array of patterns")
    api_root = f"https://api.github.com/repos/{quote(parts[0])}/{quote(parts[1])}"
    commit = request_json(f"{api_root}/commits/{quote(ref, safe='')}")
    commit_sha = str(commit.get("sha", ""))
    if not re.fullmatch(r"[0-9a-fA-F]{40,64}", commit_sha):
        raise SourceError(f"item {item['id']}: GitHub returned an invalid commit SHA")
    tree = request_json(f"{api_root}/git/trees/{quote(commit_sha)}?recursive=1")
    if tree.get("truncated"):
        raise SourceError(f"item {item['id']}: GitHub tree response was truncated")
    entries = tree.get("tree")
    if not isinstance(entries, list):
        raise SourceError(f"item {item['id']}: GitHub tree response has no entries")
    candidates: list[dict[str, Any]] = []
    prefix = f"{root}/" if root else ""
    for entry in entries:
        if not isinstance(entry, dict) or entry.get("type") != "blob":
            continue
        full_path = str(entry.get("path", ""))
        if prefix and not full_path.startswith(prefix):
            continue
        relative = full_path[len(prefix) :] if prefix else full_path
        if not relative or not pattern_matches(relative, includes):
            continue
        source_path = safe_logical_path(full_path).as_posix()
        logical_path = safe_logical_path(relative).as_posix()
        blob_sha = str(entry.get("sha", ""))
        candidates.append(
            {
                "document_id": f"{item['id']}:{relative}",
                "item_id": item["id"],
                "adapter": "github-tree",
                "source_path": source_path,
                "logical_path": logical_path,
                "requested_url": f"https://github.com/{repository}/tree/{quote(ref, safe='')}/{quote(root)}",
                "resolved_url": f"https://raw.githubusercontent.com/{repository}/{commit_sha}/{quote(source_path)}",
                "tracking_url": f"https://github.com/{repository}/blob/{quote(ref, safe='')}/{quote(source_path)}",
                "immutable_url": f"https://github.com/{repository}/blob/{commit_sha}/{quote(source_path)}",
                "revision": commit_sha,
                "upstream_object_id": blob_sha,
                "declared_media_type": mimetypes.guess_type(relative)[0] or "application/octet-stream",
                "transform": item["transform"],
            }
        )
    return deterministic_selection(candidates, item.get("selection"))


def discover_single_item(project: Path, item: dict[str, Any]) -> list[dict[str, Any]]:
    fetch = item["fetch"]
    adapter = fetch["adapter"]
    if adapter == "https":
        url = str(fetch.get("url", ""))
        if urlparse(url).scheme not in {"http", "https"}:
            raise SourceError(f"item {item['id']}: https adapter requires an HTTP(S) URL")
        name = str(item.get("output") or Path(urlparse(url).path).name or f"{item['id']}.md")
        return [
            {
                "document_id": item["id"],
                "item_id": item["id"],
                "adapter": adapter,
                "source_path": url,
                "logical_path": safe_logical_path(name).as_posix(),
                "requested_url": url,
                "resolved_url": url,
                "tracking_url": url,
                "immutable_url": None,
                "revision": None,
                "upstream_object_id": None,
                "declared_media_type": mimetypes.guess_type(urlparse(url).path)[0] or "application/octet-stream",
                "transform": item["transform"],
            }
        ]
    if adapter == "local-file":
        declared = str(fetch.get("path", ""))
        source_path = resolve_project_path(project, declared)
        name = str(item.get("output") or source_path.name)
        return [
            {
                "document_id": item["id"],
                "item_id": item["id"],
                "adapter": adapter,
                "source_path": declared,
                "local_path": str(source_path),
                "logical_path": safe_logical_path(name).as_posix(),
                "requested_url": None,
                "resolved_url": None,
                "tracking_url": None,
                "immutable_url": None,
                "revision": None,
                "upstream_object_id": None,
                "declared_media_type": mimetypes.guess_type(source_path.name)[0] or "application/octet-stream",
                "transform": item["transform"],
            }
        ]
    raise SourceError(f"item {item['id']}: unsupported adapter {adapter!r}")


def discover_documents(project: Path, manifest: dict[str, Any]) -> list[dict[str, Any]]:
    documents: list[dict[str, Any]] = []
    for item in manifest["items"]:
        if item["fetch"]["adapter"] == "github-tree":
            documents.extend(discover_github_tree(item))
        else:
            documents.extend(discover_single_item(project, item))
    seen: set[str] = set()
    for document in documents:
        document_id = document["document_id"]
        if document_id in seen:
            raise SourceError(f"duplicate expanded document id: {document_id}")
        seen.add(document_id)
    return sorted(documents, key=lambda entry: entry["document_id"])


class MarkdownHTMLParser(HTMLParser):
    """Small deterministic HTML-to-Markdown converter for source normalization."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.href_stack: list[str | None] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
            return
        if self.skip_depth:
            return
        attr_map = dict(attrs)
        if re.fullmatch(r"h[1-6]", tag):
            self.parts.append("\n\n" + "#" * int(tag[1]) + " ")
        elif tag in {"p", "div", "section", "article", "header", "footer", "blockquote"}:
            self.parts.append("\n\n")
        elif tag == "br":
            self.parts.append("  \n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag in {"ul", "ol"}:
            self.parts.append("\n")
        elif tag == "a":
            self.href_stack.append(attr_map.get("href"))
            self.parts.append("[")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag == "code":
            self.parts.append("`")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in {"script", "style", "noscript"}:
            self.skip_depth = max(0, self.skip_depth - 1)
            return
        if self.skip_depth:
            return
        if tag == "a":
            href = self.href_stack.pop() if self.href_stack else None
            self.parts.append(f"]({href})" if href else "]")
        elif tag in {"strong", "b"}:
            self.parts.append("**")
        elif tag in {"em", "i"}:
            self.parts.append("*")
        elif tag == "code":
            self.parts.append("`")
        elif re.fullmatch(r"h[1-6]", tag) or tag in {"p", "div", "section", "article", "blockquote"}:
            self.parts.append("\n\n")

    def handle_data(self, data: str) -> None:
        if not self.skip_depth:
            self.parts.append(data)

    def markdown(self) -> str:
        text = html.unescape("".join(self.parts)).replace("\r\n", "\n").replace("\r", "\n")
        text = re.sub(r"[ \t]+\n", "\n", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text.strip() + "\n"


def decode_text(data: bytes) -> str:
    try:
        return data.decode("utf-8-sig")
    except UnicodeDecodeError as exc:
        raise SourceError("source text is not valid UTF-8") from exc


def normalize_markdown(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n").rstrip() + "\n"


def transform_document(data: bytes, steps: list[dict[str, Any]], logical_path: str) -> tuple[bytes, str]:
    value: bytes | str = data
    for step in steps:
        name = step["name"]
        options = step.get("options", {})
        if not isinstance(options, dict):
            raise SourceError(f"transform {name}: options must be an object")
        if name == "markdown-copy":
            text = decode_text(value) if isinstance(value, bytes) else value
            value = normalize_markdown(text)
        elif name == "text-to-markdown":
            text = decode_text(value) if isinstance(value, bytes) else value
            title = str(options.get("title") or Path(logical_path).stem)
            value = f"# {title}\n\n{normalize_markdown(text).lstrip()}"
        elif name == "html-to-markdown":
            text = decode_text(value) if isinstance(value, bytes) else value
            parser = MarkdownHTMLParser()
            parser.feed(text)
            parser.close()
            value = parser.markdown()
        else:
            raise SourceError(f"unknown transform: {name}")
    if isinstance(value, bytes):
        raise SourceError("transformation pipeline did not produce Markdown text")
    output = normalize_markdown(value).encode("utf-8")
    fingerprint = sha256_bytes(
        canonical_json({"tool_version": TOOL_VERSION, "steps": steps}).encode("utf-8")
    )
    return output, fingerprint


def retrieve_descriptor(project: Path, descriptor: dict[str, Any]) -> tuple[bytes, dict[str, Any]]:
    if descriptor["adapter"] in {"github-tree", "https"}:
        data, metadata = request_bytes(descriptor["resolved_url"])
        return data, metadata
    if descriptor["adapter"] == "local-file":
        path = Path(descriptor["local_path"])
        try:
            data = path.read_bytes()
        except FileNotFoundError as exc:
            raise SourceError(f"local source not found: {path}") from exc
        return data, {
            "resolved_url": None,
            "media_type": descriptor["declared_media_type"],
            "etag": None,
            "last_modified": datetime.fromtimestamp(path.stat().st_mtime, timezone.utc).isoformat(),
        }
    raise SourceError(f"unsupported adapter: {descriptor['adapter']}")


def artifact_paths(
    project: Path,
    raw_root: Path,
    manifest: dict[str, Any],
    descriptor: dict[str, Any],
    input_hash: str,
    output_hash: str,
) -> tuple[Path, Path, Path]:
    storage = manifest.get("storage", {})
    original_area = "retained" if storage.get("originals", "reference-only") == "vendored" else "cache"
    normalized_area = "retained" if storage.get("normalized", "reference-only") == "vendored" else "cache"
    suffix = Path(descriptor["logical_path"]).suffix or ".bin"
    original = raw_root / original_area / "objects" / input_hash / f"original{suffix}"
    normalized = raw_root / normalized_area / "outputs" / output_hash / "document.md"
    materialized = raw_root / "cache" / "documents" / Path(*safe_logical_path(descriptor["logical_path"]).parts)
    return original, normalized, materialized


def write_verified(path: Path, data: bytes, expected_hash: str) -> None:
    if sha256_bytes(data) != expected_hash:
        raise SourceError(f"refusing to write hash-mismatched data to {path}")
    if path.exists():
        current = path.read_bytes()
        if sha256_bytes(current) != expected_hash:
            raise SourceError(f"existing immutable artifact has wrong hash: {path}")
        return
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(delete=False, dir=path.parent, prefix=f".{path.name}.", suffix=".tmp") as handle:
        temp_path = Path(handle.name)
        handle.write(data)
        handle.flush()
        os.fsync(handle.fileno())
    try:
        os.replace(temp_path, path)
    finally:
        if temp_path.exists():
            temp_path.unlink()


def make_lock_document(
    project: Path,
    raw_root: Path,
    manifest: dict[str, Any],
    descriptor: dict[str, Any],
    input_data: bytes,
    retrieval_metadata: dict[str, Any],
    output_data: bytes,
    pipeline_fingerprint: str,
    *,
    write_artifacts: bool,
) -> dict[str, Any]:
    input_hash = sha256_bytes(input_data)
    output_hash = sha256_bytes(output_data)
    original, normalized, materialized = artifact_paths(
        project, raw_root, manifest, descriptor, input_hash, output_hash
    )
    if write_artifacts:
        write_verified(original, input_data, input_hash)
        write_verified(normalized, output_data, output_hash)
        write_verified(materialized, output_data, output_hash)
    return {
        "document_id": descriptor["document_id"],
        "item_id": descriptor["item_id"],
        "adapter": descriptor["adapter"],
        "source_path": descriptor["source_path"],
        "logical_path": descriptor["logical_path"],
        "retrieval": {
            "requested_url": descriptor.get("requested_url"),
            "resolved_url": retrieval_metadata.get("resolved_url") or descriptor.get("resolved_url"),
            "tracking_url": descriptor.get("tracking_url"),
            "immutable_url": descriptor.get("immutable_url"),
            "revision": descriptor.get("revision"),
            "upstream_object_id": descriptor.get("upstream_object_id"),
            "retrieved_at": now_utc(),
            "media_type": retrieval_metadata.get("media_type") or descriptor["declared_media_type"],
            "etag": retrieval_metadata.get("etag"),
            "last_modified": retrieval_metadata.get("last_modified"),
            "size": len(input_data),
            "sha256": input_hash,
        },
        "transformation": {
            "steps": copy.deepcopy(descriptor["transform"]),
            "pipeline_fingerprint": pipeline_fingerprint,
            "output_sha256": output_hash,
        },
        "artifacts": {
            "original_path": project_relative(project, original),
            "normalized_path": project_relative(project, normalized),
            "materialized_path": project_relative(project, materialized),
        },
        "lifecycle": {
            "state": LIFECYCLE_ACTIVE,
            "refresh_policy": "automatic",
            "last_successful_retrieval": now_utc(),
        },
    }


def load_source(project: Path, source_id: str) -> tuple[dict[str, Any], dict[str, Any] | None, Path, Path, Path]:
    manifest_path, lock_path, raw_root = source_paths(project, source_id)
    manifest = read_json(manifest_path)
    validate_manifest(manifest, source_id)
    lock = read_json(lock_path) if lock_path.exists() else None
    return manifest, lock, manifest_path, lock_path, raw_root


def compare_documents(old_docs: dict[str, dict[str, Any]], new_docs: dict[str, dict[str, Any]]) -> dict[str, list[str]]:
    added: list[str] = []
    changed: list[str] = []
    unchanged: list[str] = []
    removed: list[str] = []
    for document_id, document in sorted(new_docs.items()):
        old = old_docs.get(document_id)
        if old is None:
            added.append(document_id)
        elif (
            old.get("transformation", {}).get("output_sha256")
            != document.get("transformation", {}).get("output_sha256")
            or old.get("transformation", {}).get("pipeline_fingerprint")
            != document.get("transformation", {}).get("pipeline_fingerprint")
        ):
            changed.append(document_id)
        else:
            unchanged.append(document_id)
    for document_id in sorted(set(old_docs) - set(new_docs)):
        removed.append(document_id)
    return {"added": added, "changed": changed, "unchanged": unchanged, "removed": removed}


def refresh_source(
    project: Path,
    source_id: str,
    *,
    dry_run: bool = False,
    include_archived: bool = False,
    target_document: str | None = None,
) -> dict[str, Any]:
    manifest, old_lock, _manifest_path, lock_path, raw_root = load_source(project, source_id)
    old_docs = {
        document["document_id"]: document
        for document in (old_lock or {}).get("documents", [])
        if isinstance(document, dict) and isinstance(document.get("document_id"), str)
    }
    descriptors = discover_documents(project, manifest)
    if target_document:
        descriptors = [entry for entry in descriptors if entry["document_id"] == target_document]
        if not descriptors:
            raise SourceError(f"document is not present in current source discovery: {target_document}")
    next_docs = dict(old_docs) if target_document else {}
    failures: list[dict[str, str]] = []
    processed: set[str] = set()
    for descriptor in descriptors:
        document_id = descriptor["document_id"]
        processed.add(document_id)
        old = old_docs.get(document_id)
        old_state = (old or {}).get("lifecycle", {}).get("state")
        if old_state == LIFECYCLE_ARCHIVED and not include_archived:
            next_docs[document_id] = old
            continue
        try:
            input_data, metadata = retrieve_descriptor(project, descriptor)
            output_data, fingerprint = transform_document(
                input_data, descriptor["transform"], descriptor["logical_path"]
            )
            next_docs[document_id] = make_lock_document(
                project,
                raw_root,
                manifest,
                descriptor,
                input_data,
                metadata,
                output_data,
                fingerprint,
                write_artifacts=not dry_run,
            )
        except SourceError as exc:
            failures.append({"document_id": document_id, "error": str(exc)})
    if failures:
        return {
            "ok": False,
            "operation": "check" if dry_run else "refresh",
            "source_id": source_id,
            "failures": failures,
            "lock_updated": False,
        }
    discovery_removed: set[str] = set()
    if not target_document:
        for document_id, old in old_docs.items():
            if document_id in processed:
                continue
            discovery_removed.add(document_id)
            preserved = copy.deepcopy(old)
            if preserved.get("lifecycle", {}).get("state") != LIFECYCLE_ARCHIVED:
                preserved["lifecycle"] = {
                    **preserved.get("lifecycle", {}),
                    "state": LIFECYCLE_SUSPECTED,
                    "refresh_policy": "automatic",
                    "suspected_at": now_utc(),
                    "reason": "document was not present in current source discovery",
                }
            next_docs[document_id] = preserved
    changes = compare_documents(old_docs, next_docs)
    if discovery_removed:
        changes["removed"] = sorted(discovery_removed)
        changes["unchanged"] = [
            document_id for document_id in changes["unchanged"] if document_id not in discovery_removed
        ]
    lock = {
        "schema_version": SCHEMA_VERSION,
        "source_id": source_id,
        "manifest_sha256": sha256_bytes(canonical_json(manifest).encode("utf-8")),
        "updated_at": now_utc(),
        "documents": [next_docs[key] for key in sorted(next_docs)],
    }
    if not dry_run:
        atomic_write_json(lock_path, lock)
        changes_dir = lock_path.parent / "changes"
        change_key = now_utc().replace(":", "").replace("+00:00", "Z")
        atomic_write_json(
            changes_dir / f"{change_key}.json",
            {"schema_version": SCHEMA_VERSION, "source_id": source_id, "changes": changes},
        )
    return {
        "ok": True,
        "operation": "check" if dry_run else "refresh",
        "source_id": source_id,
        "document_count": len(next_docs),
        "changes": changes,
        "lock_updated": not dry_run,
    }


def hydrate_source(project: Path, source_id: str) -> dict[str, Any]:
    manifest, lock, _manifest_path, _lock_path, raw_root = load_source(project, source_id)
    if lock is None:
        raise SourceError("cannot hydrate without a source.lock.json; run refresh first")
    hydrated: list[str] = []
    skipped_archived: list[str] = []
    failures: list[dict[str, str]] = []
    for document in lock.get("documents", []):
        document_id = document["document_id"]
        state = document.get("lifecycle", {}).get("state")
        artifacts = document.get("artifacts", {})
        expected_input = document.get("retrieval", {}).get("sha256")
        expected_output = document.get("transformation", {}).get("output_sha256")
        if state == LIFECYCLE_ARCHIVED:
            try:
                original = resolve_project_path(project, artifacts["original_path"])
                normalized = resolve_project_path(project, artifacts["normalized_path"])
                if sha256_bytes(original.read_bytes()) != expected_input:
                    raise SourceError("retained original hash mismatch")
                output_data = normalized.read_bytes()
                if sha256_bytes(output_data) != expected_output:
                    raise SourceError("retained normalized hash mismatch")
                materialized = raw_root / "cache" / "documents" / Path(
                    *safe_logical_path(document["logical_path"]).parts
                )
                write_verified(materialized, output_data, expected_output)
                skipped_archived.append(document_id)
            except (KeyError, FileNotFoundError, SourceError) as exc:
                failures.append({"document_id": document_id, "error": str(exc)})
            continue
        try:
            adapter = document["adapter"]
            retrieval = document["retrieval"]
            if adapter in {"github-tree", "https"}:
                input_data, _metadata = request_bytes(retrieval["resolved_url"])
            elif adapter == "local-file":
                input_data = resolve_project_path(project, document["source_path"]).read_bytes()
            else:
                raise SourceError(f"unsupported locked adapter: {adapter}")
            if sha256_bytes(input_data) != expected_input:
                raise SourceError("retrieved input does not match locked SHA-256")
            output_data, fingerprint = transform_document(
                input_data, document["transformation"]["steps"], document["logical_path"]
            )
            if fingerprint != document["transformation"]["pipeline_fingerprint"]:
                raise SourceError("transformation fingerprint does not match lock")
            if sha256_bytes(output_data) != expected_output:
                raise SourceError("transformed output does not match locked SHA-256")
            original, normalized, materialized = artifact_paths(
                project, raw_root, manifest, document, expected_input, expected_output
            )
            write_verified(original, input_data, expected_input)
            write_verified(normalized, output_data, expected_output)
            write_verified(materialized, output_data, expected_output)
            hydrated.append(document_id)
        except (KeyError, FileNotFoundError, SourceError) as exc:
            failures.append({"document_id": document_id, "error": str(exc)})
    return {
        "ok": not failures,
        "operation": "hydrate",
        "source_id": source_id,
        "hydrated": hydrated,
        "archived_materialized": skipped_archived,
        "failures": failures,
    }


def verify_hash(path: Path, expected: str, label: str, issues: list[str]) -> None:
    if not path.exists():
        issues.append(f"missing {label}: {path}")
        return
    if not path.is_file():
        issues.append(f"{label} is not a file: {path}")
        return
    if sha256_bytes(path.read_bytes()) != expected:
        issues.append(f"hash mismatch for {label}: {path}")


def validate_source(project: Path, source_id: str, mode: str) -> dict[str, Any]:
    manifest, lock, _manifest_path, _lock_path, _raw_root = load_source(project, source_id)
    issues: list[str] = []
    if lock is None:
        issues.append("source.lock.json is missing")
        return {"ok": False, "mode": mode, "source_id": source_id, "issues": issues}
    expected_manifest_hash = sha256_bytes(canonical_json(manifest).encode("utf-8"))
    if lock.get("manifest_sha256") != expected_manifest_hash:
        issues.append("manifest hash differs from source.lock.json; refresh is required")
    seen: set[str] = set()
    storage = manifest.get("storage", {})
    for document in lock.get("documents", []):
        document_id = document.get("document_id")
        if not isinstance(document_id, str) or document_id in seen:
            issues.append(f"invalid or duplicate document_id: {document_id!r}")
            continue
        seen.add(document_id)
        state = document.get("lifecycle", {}).get("state")
        if state not in {LIFECYCLE_ACTIVE, LIFECYCLE_SUSPECTED, LIFECYCLE_ARCHIVED}:
            issues.append(f"{document_id}: invalid lifecycle state {state!r}")
        retrieval = document.get("retrieval", {})
        transform = document.get("transformation", {})
        artifacts = document.get("artifacts", {})
        input_hash = retrieval.get("sha256")
        output_hash = transform.get("output_sha256")
        if not re.fullmatch(r"[0-9a-f]{64}", str(input_hash)):
            issues.append(f"{document_id}: invalid input SHA-256")
            continue
        if not re.fullmatch(r"[0-9a-f]{64}", str(output_hash)):
            issues.append(f"{document_id}: invalid output SHA-256")
            continue
        require_original = mode == "hydrated" or state == LIFECYCLE_ARCHIVED or storage.get("originals") == "vendored"
        require_normalized = mode == "hydrated" or state == LIFECYCLE_ARCHIVED or storage.get("normalized") == "vendored"
        try:
            if require_original:
                verify_hash(
                    resolve_project_path(project, artifacts["original_path"]), input_hash, f"{document_id} original", issues
                )
            if require_normalized:
                verify_hash(
                    resolve_project_path(project, artifacts["normalized_path"]), output_hash, f"{document_id} normalized", issues
                )
            if mode == "hydrated":
                verify_hash(
                    resolve_project_path(project, artifacts["materialized_path"]), output_hash, f"{document_id} materialized", issues
                )
        except (KeyError, SourceError) as exc:
            issues.append(f"{document_id}: invalid artifact path: {exc}")
    return {
        "ok": not issues,
        "mode": mode,
        "source_id": source_id,
        "document_count": len(seen),
        "issues": issues,
    }


def source_status(project: Path, source_id: str) -> dict[str, Any]:
    _manifest, lock, manifest_path, lock_path, _raw_root = load_source(project, source_id)
    counts = {LIFECYCLE_ACTIVE: 0, LIFECYCLE_SUSPECTED: 0, LIFECYCLE_ARCHIVED: 0}
    for document in (lock or {}).get("documents", []):
        state = document.get("lifecycle", {}).get("state")
        counts[state] = counts.get(state, 0) + 1
    return {
        "ok": True,
        "source_id": source_id,
        "manifest": str(manifest_path.resolve()),
        "lock": str(lock_path.resolve()),
        "locked": lock is not None,
        "document_count": sum(counts.values()),
        "lifecycle_counts": counts,
    }


def mark_unavailable(project: Path, source_id: str, document_id: str, reason: str) -> dict[str, Any]:
    _manifest, lock, _manifest_path, lock_path, raw_root = load_source(project, source_id)
    if lock is None:
        raise SourceError("cannot archive a source without a lock")
    documents = lock.get("documents", [])
    target = next((doc for doc in documents if doc.get("document_id") == document_id), None)
    if target is None:
        raise SourceError(f"unknown locked document: {document_id}")
    if target.get("lifecycle", {}).get("state") == LIFECYCLE_ARCHIVED:
        raise SourceError(f"document is already archived-unavailable: {document_id}")
    artifacts = target["artifacts"]
    input_hash = target["retrieval"]["sha256"]
    output_hash = target["transformation"]["output_sha256"]
    original = resolve_project_path(project, artifacts["original_path"])
    normalized = resolve_project_path(project, artifacts["normalized_path"])
    if not original.exists() or sha256_bytes(original.read_bytes()) != input_hash:
        raise SourceError("last retrieved original is missing or hash-mismatched; cannot preserve it")
    if not normalized.exists() or sha256_bytes(normalized.read_bytes()) != output_hash:
        raise SourceError("last normalized output is missing or hash-mismatched; cannot preserve it")
    archive_root = raw_root / "retained" / "archive" / safe_component(document_id) / output_hash
    original_suffix = original.suffix or ".bin"
    retained_original = archive_root / f"original{original_suffix}"
    retained_normalized = archive_root / "normalized.md"
    write_verified(retained_original, original.read_bytes(), input_hash)
    write_verified(retained_normalized, normalized.read_bytes(), output_hash)
    provenance = {
        "schema_version": SCHEMA_VERSION,
        "archived_at": now_utc(),
        "reason": reason,
        "source_id": source_id,
        "document": copy.deepcopy(target),
        "retained": {
            "original_path": project_relative(project, retained_original),
            "normalized_path": project_relative(project, retained_normalized),
        },
    }
    provenance_path = archive_root / "provenance.json"
    atomic_write_json(provenance_path, provenance)
    target["artifacts"]["original_path"] = project_relative(project, retained_original)
    target["artifacts"]["normalized_path"] = project_relative(project, retained_normalized)
    target["lifecycle"] = {
        **target.get("lifecycle", {}),
        "state": LIFECYCLE_ARCHIVED,
        "refresh_policy": "manual",
        "declared_at": now_utc(),
        "reason": reason,
        "provenance_path": project_relative(project, provenance_path),
    }
    lock["updated_at"] = now_utc()
    atomic_write_json(lock_path, lock)
    return {
        "ok": True,
        "operation": "mark-unavailable",
        "source_id": source_id,
        "document_id": document_id,
        "retained_original": str(retained_original.resolve()),
        "retained_normalized": str(retained_normalized.resolve()),
        "provenance": str(provenance_path.resolve()),
        "git_action": "review and commit retained evidence, source.lock.json, and provenance.json",
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--version", action="version", version=TOOL_VERSION)
    sub = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (
        ("status", "show committed source and lifecycle status without network access"),
        ("check", "retrieve and transform current sources without changing local state"),
        ("refresh", "retrieve current sources and atomically advance the source lock"),
        ("hydrate", "reconstruct the exact committed source lock"),
    ):
        command = sub.add_parser(name, help=help_text)
        command.add_argument("--project", required=True)
        command.add_argument("--source", required=True)
        if name == "refresh":
            command.add_argument("--include-archived", action="store_true")
            command.add_argument("--document")
    command = sub.add_parser("validate", help="validate portable metadata or a fully hydrated source")
    command.add_argument("--project", required=True)
    command.add_argument("--source", required=True)
    command.add_argument("--mode", choices=("portable", "hydrated"), default="portable")
    command = sub.add_parser("mark-unavailable", help="retain last verified evidence and require manual refresh")
    command.add_argument("--project", required=True)
    command.add_argument("--source", required=True)
    command.add_argument("--document", required=True)
    command.add_argument("--reason", required=True)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    project = Path(args.project).expanduser().resolve()
    if not project.is_dir():
        print(json.dumps({"ok": False, "error": f"project directory not found: {project}"}, indent=2), file=sys.stderr)
        return 2
    try:
        if args.command == "status":
            result = source_status(project, args.source)
        elif args.command == "check":
            result = refresh_source(project, args.source, dry_run=True)
        elif args.command == "refresh":
            result = refresh_source(
                project,
                args.source,
                include_archived=args.include_archived,
                target_document=args.document,
            )
        elif args.command == "hydrate":
            result = hydrate_source(project, args.source)
        elif args.command == "validate":
            result = validate_source(project, args.source, args.mode)
        elif args.command == "mark-unavailable":
            result = mark_unavailable(project, args.source, args.document, args.reason)
        else:
            raise SourceError(f"unsupported command: {args.command}")
    except (KeyError, TypeError, ValueError, SourceError) as exc:
        print(json.dumps({"ok": False, "error": str(exc)}, indent=2), file=sys.stderr)
        return 1
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0 if result.get("ok") else 1


if __name__ == "__main__":
    raise SystemExit(main())
