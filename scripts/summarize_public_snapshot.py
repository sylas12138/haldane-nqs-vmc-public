"""Generate a small Markdown report from the public Haldane audit snapshot."""

from __future__ import annotations

import csv
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "public_audit_snapshot.csv"
OUT = ROOT / "docs" / "generated_public_report.md"


def main() -> None:
    rows = list(csv.DictReader(DATA.open(newline="", encoding="utf-8")))
    verdicts = Counter(row["public_verdict"] for row in rows)
    replay = Counter(row["replay_status"] for row in rows)

    lines = [
        "# Generated Public Snapshot Report",
        "",
        "This file is generated from `data/public_audit_snapshot.csv`.",
        "It is a public, sanitized report and not the full private result table.",
        "",
        "## Counts",
        "",
        f"- rows: {len(rows)}",
        f"- interaction values: {', '.join(row['V'] for row in rows)}",
        "",
        "## Verdict Counts",
        "",
    ]
    for key, value in sorted(verdicts.items()):
        lines.append(f"- `{key}`: {value}")

    lines += ["", "## Replay Status", ""]
    for key, value in sorted(replay.items()):
        lines.append(f"- `{key}`: {value}")

    lines += [
        "",
        "## Rows",
        "",
        "| row_id | V | role | public_verdict | replay_status |",
        "|---|---:|---|---|---|",
    ]
    for row in rows:
        lines.append(
            f"| {row['row_id']} | {row['V']} | {row['role']} | "
            f"{row['public_verdict']} | {row['replay_status']} |"
        )

    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
