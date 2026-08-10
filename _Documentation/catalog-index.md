# Catalog Index

The repository root `index.html` is a standalone catalog landing page. Each card represents a direct-child OKF project and links to `<project>/okf/catalog/viz.html` using a repository-relative URL.

The page intentionally uses embedded HTML and CSS so it works directly from a local checkout and from static hosting without a build step. When a catalog project is added, renamed, or removed, update its corresponding card in `index.html`.

The visual treatment references the published Ossenna.Space `Satellite Visualizer` background from the Ossenna Squarespace CDN and provides a black fallback underneath it. The Ossenna.Space masthead links to `https://www.ossenna.space`.
