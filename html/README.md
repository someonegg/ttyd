# Frontend development

The repository includes a prebuilt `html/dist/inline.html` and its embedded version in `src/html.h`. These instructions are only needed when modifying or rebuilding the frontend.

## Prerequisites

Install Node.js 18 or later with Corepack. If `corepack` is unavailable, run `npm install --global corepack`.

From the `html` directory, install dependencies using the Yarn version pinned in `package.json`:

```bash
corepack yarn install --immutable
```

## Development

1. Start ttyd: `ttyd --writable bash`
2. From the `html` directory, start the dev server: `corepack yarn run start`.
3. Open `http://localhost:9000`.

## Build

Run `corepack yarn run build` from the `html` directory. This generates `dist/inline.html` and embeds it in `../src/html.h`.

Rebuild the C server afterward to include the updated frontend. Commit both generated files when updating the bundled frontend. To serve the HTML directly instead, run `ttyd --writable --index ./html/dist/inline.html bash` from the repository root.

## Test

Run unit tests from the `html` directory: `corepack yarn test:unit`.
