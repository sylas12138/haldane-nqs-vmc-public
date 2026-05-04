# Benchmark Protocol

## Small-system ED Benchmark

For ED-accessible clusters, the benchmark workflow is:

1. define Hamiltonian, boundary condition, filling, and observable convention;
2. compute exact or high-confidence reference values;
3. train NQS/VMC candidate;
4. compare energy, CDW, Q2, topology diagnostic, and variance;
5. replay candidate checkpoints independently;
6. classify the candidate as benchmark-supported, diagnostic-only, or not stable.

## Larger-system VMC Audit

For larger systems without full ED:

1. anchor easy limits such as noninteracting or weak-interaction points;
2. use internally consistent observable trends;
3. avoid promoting a single checkpoint without replay;
4. mark topology outputs as diagnostics unless a many-body topology protocol is completed;
5. keep finite-size and estimator caveats explicit.

## Public / Private Split

Public:

- model definition;
- observable convention;
- methodology description;
- small demonstration code;
- application-oriented project summary.

Private:

- raw result trees;
- checkpoints;
- remote scripts and paths;
- detailed experiment logs;
- failure ledgers;
- agent operating rules.

