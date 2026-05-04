# Generated Public Snapshot Report

This file is generated from `data/public_audit_snapshot.csv`.
It is a public, sanitized report and not the full private result table.

## Counts

- rows: 5
- interaction values: 1.11, 1.13, 1.15, 1.17, 1.19

## Verdict Counts

- `benchmark_supporting_row`: 1
- `diagnostic_row_not_final_claim`: 1
- `method_diagnostic_row`: 2
- `reviewer_grade_finite_size_anchor`: 1

## Replay Status

- `replay_checked`: 3
- `replay_sensitive`: 1
- `strict_replay_pass`: 1

## Rows

| row_id | V | role | public_verdict | replay_status |
|---|---:|---|---|---|
| H-L3-V111 | 1.11 | CI-side near-boundary check | benchmark_supporting_row | replay_checked |
| H-L3-V113 | 1.13 | finite-size transition window | diagnostic_row_not_final_claim | replay_sensitive |
| H-L3-V115 | 1.15 | near-critical anchor | reviewer_grade_finite_size_anchor | strict_replay_pass |
| H-L3-V117 | 1.17 | CDW-side audit candidate | method_diagnostic_row | replay_checked |
| H-L3-V119 | 1.19 | CDW-side audit candidate | method_diagnostic_row | replay_checked |
