# Quack downloads

Public, signed macOS releases of Quack. Application source is maintained separately.

Download Quack at https://updates.tired.dev/quack.

Release assets contain installers, signed Sparkle update archives, and revision-pinned speech models. Model releases are separate prereleases so they do not become the latest app release.

`site/` contains only public website files, signed update feeds, and release records. `redirects/` preserves older download URLs. Cloudflare Workers Static Assets serves these files without Worker code, R2 reads, or runtime database access.

The deployment workflow serializes publications and checks out the latest `main` when each job starts. The publisher must push without force. If another release changes `main` first, retry publication from the current state. Old release assets must remain available for clients that already fetched an earlier feed.

The workflow uses the repository secret `CLOUDFLARE_API_TOKEN`, scoped to Workers Scripts editing in the publishing account. If routes are configured, it also needs Workers Routes editing and Zone reading for tired.dev. No credential belongs in this repository's files. The deployment check rejects Worker entrypoints, Worker-first asset routing, R2 bindings, and path routes that miss query strings.

Phonon-2 weights are distributed under CC-BY-4.0 by Fermion Research, derived from NVIDIA Parakeet TDT 0.6B v3. The original NOTICE and license are separate model-release assets and are bundled in the app. Quack's public downloads do not grant an open-source license to Quack itself.
