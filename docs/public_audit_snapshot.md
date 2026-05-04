# Public Audit Snapshot

This page gives a small public-facing snapshot of the internal audit style used in the interacting Haldane NQS/VMC project.

It is not a full result table. It removes private run names, raw checkpoint paths, remote-cluster details, failure ledgers, and unfinished experiment records. The goal is to show the kind of evidence I track before trusting a variational result.

## What Is Audited

For each candidate row, the internal table separates:

- model and finite cluster;
- interaction value `V`;
- training-best energy;
- strict replay energy;
- sublattice-order diagnostics `CDW=<|Q|>` and `Q2=<Q^2>`;
- topology diagnostic level;
- source provenance;
- pass/fail status and reason.

The key habit is simple: a low training energy is not enough. A report-grade row must survive fresh evaluation and must make sense across energy, order, and topology.

## Public Aggregate Snapshot

The current internal near-critical table has the following high-level status:

| item | public value |
|---|---:|
| extracted audit rows | 21 |
| covered interaction values | `V=1.11, 1.13, 1.14, 1.15, 1.17, 1.19` |
| rows with explicit source provenance | 21 |
| strict pass rows at the time of extraction | 1 |
| contract-failed or not-yet-closed rows | 20 |

The main lesson from this table is not that the project has a final phase diagram. It is that near the competing CI/CDW boundary, many candidate runs can look useful in one diagnostic and fail another. That is why the project treats negative rows as evidence about the method, not just as failed attempts.

## Representative Public Row

The following row is deliberately rounded and anonymized. It is included to show the audit schema, not to publish a final numerical result.

| cluster | filling | `V` | role | audit status | public interpretation |
|---|---:|---:|---|---|---|
| `L=3` honeycomb | half filling | `1.15` | near-critical anchor | strict replay pass in the internal table | useful finite-size benchmark row; still not a thermodynamic claim |

For this kind of row, I check whether the energy, `CDW`, `Q2`, and topology diagnostic tell a consistent story. If one channel disagrees, the row is treated as a diagnostic case rather than a finished physics conclusion.

## Common Failure Labels

The internal table uses a restricted failure vocabulary. Publicly, the main categories are:

- energy looks acceptable but order is wrong;
- order looks acceptable but topology diagnostic is not reliable;
- optimizer or sampler instability prevents replay;
- checkpoint selection is optimistic relative to fresh replay;
- ansatz family has a visible branch bias.

These labels help decide the next experiment. For example, an energy/order mismatch suggests a different ansatz or branch initialization, while replay instability suggests a sampler or checkpoint audit problem.

## Claim Boundary

Safe public statement:

> I built an audit workflow showing that interacting Haldane NQS/VMC results near the CI/CDW boundary must be judged by energy, order, topology, and replay together.

Unsafe statement:

> This public repository proves a final interacting Haldane phase diagram.

That second statement is intentionally not made here.
