# Juns Page V2

Juns Page V2 is a local visual and product experiment for a future `juns.page`. It is a content-first personal homepage built entirely from local Markdown and YAML, with no runtime backend, analytics, authentication, remote fonts, or connected accounts.

This repository does not configure deployment. The prototype is not a published version of `juns.page`.

## Stack

- React 19 and TypeScript
- React Router 8 Framework Mode
- Static prerendering with no runtime server
- Vite+ `0.3.0`, installed project-locally and invoked through its exact `vp` binary
- CSS Modules plus small global token and reset files
- Bun for dependency and script management

## Routes

Public, statically prerendered routes:

- `/` — identity, recent notes, and direct project/collection links
- `/stack` — public tools and services catalog
- `/sites` — public resource collection
- `/til` — five sourced notes
- `/computer` — six practical workflow tips
- `/listening` — manual collection state and three labeled sample rows

Build-time experimental route:

- `/workflows` — keyboard-capable Evidence Ledger workflow sample

The workflow route is omitted from the route table, navigation, and prerender list in the default build. Enable it for one command by setting the non-public build variable:

```bash
ENABLE_EXPERIMENTS=true bun run dev
ENABLE_EXPERIMENTS=true bun run build
```

`.env.example` documents the switch without enabling it.

## Local development

```bash
bun install
bun run dev
```

The scripts resolve the project-local `node_modules/.bin/vp`; no global Vite+ install or ambiguous default package binary is required.

## Verification and static output

```bash
bun run typecheck
bun run build
```

A successful production build writes the static site to `build/client/`, including an HTML file for every registered route. Markdown and YAML in `content/` are parsed during the build and bundled into the generated pages.

Deployment, hosting, and domain binding are intentionally not configured.
