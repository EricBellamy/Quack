import json
from pathlib import Path

root = Path(__file__).resolve().parents[1]
config = json.loads((root / "wrangler.json").read_text())
if "main" in config or config.get("assets", {}).get("run_worker_first") or config.get("r2_buckets"):
    raise ValueError("Update hosting must serve static assets directly, without Worker code or R2 bindings.")
for route in config.get("routes", []):
    if "/" in route["pattern"] and not route["pattern"].endswith("*"):
        raise ValueError("Path routes must end in * so query strings do not fall through to the old origin.")
lines = []
seen = set()
for path in sorted((root / "redirects").glob("*.txt")):
    for line in path.read_text().splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        source, target, status = line.split()
        if source in seen or not source.startswith("/") or not target.startswith("https://github.com/") or status != "302":
            raise ValueError(f"Invalid or duplicate download redirect: {line}")
        seen.add(source)
        lines.append(line)
(root / "site/_redirects").write_text("\n".join(lines) + "\n")
for path in (root / "site").rglob("*"):
    if path.is_file() and path.stat().st_size > 25 * 1024 * 1024:
        raise ValueError(f"Binary downloads belong in Releases, not static hosting: {path}")
