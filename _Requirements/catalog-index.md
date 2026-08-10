# Catalog Index Requirements

## R-INDEX-001 Catalog discovery

The repository root shall provide an `index.html` page listing every direct-child OKF catalog project that contains `okf/catalog/viz.html`.

## R-INDEX-002 Visualization navigation

Each catalog entry shall provide a relative hotlink to that project's `okf/catalog/viz.html` page so the index remains usable from a local checkout or static web host.

## R-INDEX-003 Standalone operation

The catalog index shall render without a build step, server-side processing, or external runtime dependency.

## R-INDEX-004 Ossenna.Space branding

The catalog index shall prominently identify Ossenna.Space, link to `https://www.ossenna.space`, and visually reference the background published on the Ossenna Space page while retaining a usable fallback when the remote image is unavailable.
