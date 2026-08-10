# Pages Publishing

`.github/workflows/static.yml` deploys the complete repository as a static GitHub Pages artifact after pushes to `main` and when manually dispatched.

The workflow uses Node 24-compatible action majors:

- `actions/checkout@v7`
- `actions/configure-pages@v6`
- `actions/upload-pages-artifact@v5`
- `actions/deploy-pages@v5`

When GitHub deprecates a runner JavaScript runtime, update these action references to maintained releases that natively target the replacement runtime. Do not suppress runtime warnings by opting back into an end-of-life Node.js version.
