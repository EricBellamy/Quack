from pathlib import Path

root = Path(__file__).resolve().parents[1]
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
