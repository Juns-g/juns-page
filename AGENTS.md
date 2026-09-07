# juns-page Agent Guidelines

This repository hosts the static source and Cloudflare Pages deployment for `juns.page`.

## Development & Verification Rules

1. **No Live-Reload Pushes**:
   - Never push commits to `main` or remote branches solely to preview or test frontend UI, deep links, or functions.
   - Do not treat Cloudflare Pages build runs as a live-reload testing tool.

2. **Local & LAN First Testing**:
   - **Static Pages & Deep Link Jumpers (`/go/*`)**:
     Run a local server bound to all interfaces:
     ```bash
     python3 -m http.server 8080 --bind 0.0.0.0
     ```
     Test directly on mobile devices within the same Wi-Fi using the Mac LAN IP (e.g. `http://<LAN-IP>:8080/go/<platform>/`).
   - **Pages Functions (`/functions/api/*`)**:
     Run the Cloudflare local dev environment:
     ```bash
     npx wrangler pages dev . --ip 0.0.0.0 --port 8788
     ```
   - **Public HTTPS / Universal Link Testing (if strictly needed)**:
     Use an ad-hoc local tunnel (e.g., `cloudflared tunnel --url http://127.0.0.1:8080`) rather than pushing to production.

3. **Commit & Deployment Discipline**:
   - Perform iterative changes, bug fixes, and parameter tweaks locally.
   - Verify on local/LAN devices first.
   - Once verified, organize changes into clean, atomic commits and push only when the feature or fix is complete.
