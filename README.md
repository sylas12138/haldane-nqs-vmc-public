# Interacting Haldane Model NQS/VMC Benchmark

Public research portfolio for Neural Quantum States (NQS) and Variational Monte Carlo (VMC) on the interacting spinless-fermion Haldane model.

This repository is intended for graduate-application and academic-communication use. It describes the physical problem, benchmark logic, observable conventions, ansatz design, and reproducibility scaffold. It intentionally does **not** include raw checkpoints, full result trees, remote-cluster paths, experiment logs, failure ledgers, or private agent instructions.

## 1. Scientific Motivation

The Haldane model on a honeycomb lattice is a minimal model of a Chern insulator. Adding nearest-neighbor repulsion creates competition between a topological Chern-insulator branch and a charge-density-wave (CDW) branch. Near the transition, an NQS/VMC calculation can look deceptively good if one only tracks energy: the wavefunction may have low variational energy while remaining in the wrong topological or charge-order basin.

This makes the interacting Haldane model a useful benchmark for AI4S and NQS research:

- it is small enough to benchmark against exact diagonalization on finite clusters;
- it contains topological and symmetry-breaking physics in one model;
- it exposes multi-basin optimization, checkpoint selection, and observable mismatch;
- it connects method development to physically meaningful diagnostics.

## 2. Model

The studied system is the spinless-fermion Haldane model with nearest-neighbor repulsion on the honeycomb lattice:

```text
H = -t1 sum_<ij> (c_i^dagger c_j + h.c.)
    -t2 sum_<<ij>> (exp(i phi nu_ij) c_i^dagger c_j + h.c.)
    +V sum_<ij> n_i n_j
```

Typical benchmark setting:

- honeycomb lattice;
- half filling;
- complex next-nearest-neighbor hopping phase `phi`;
- nearest-neighbor repulsion `V`;
- finite clusters where ED can be used as a benchmark;
- larger clusters where VMC must be audited internally.

## 3. Observable Convention

For half filling, define the A/B sublattice imbalance

```text
Q = (N_A - N_B) / (N / 2)
CDW = <|Q|>
Q2 = <Q^2>
```

`CDW` and `Q2` are symmetry-even amplitude diagnostics. They are not the signed order parameter `<N_A-N_B>`. A finite-size Chern-insulator state can have nonzero `CDW` and `Q2` from sublattice occupation fluctuations. Evidence for true CDW enhancement must be read relative to the finite-size baseline and checked against energy and topology diagnostics.

## 4. NQS/VMC Methodology

The project uses NQS/VMC as a controlled variational method rather than a black-box optimizer. Main ansatz ideas explored in the private research workspace include:

- Slater-Jastrow baselines;
- neural backflow corrections;
- orbital-mixing references;
- CI/CDW multi-reference branches;
- source-free direct Hamiltonian learning on ED-sized clusters;
- GNN-style size transfer and teacher-bias transfer;
- strict replay / fresh-walker evaluation.

The central methodological point is that report-grade results must compare multiple observables:

- energy per site;
- `CDW=<|Q|>`;
- `Q2=<Q^2>`;
- topology diagnostic;
- variance / local-energy stability;
- strict replay stability.

## 5. Public Repository Contents

```text
docs/
  model_and_observables.md      model, Hamiltonian, observable definitions
  nqs_vmc_methodology.md        ansatz and benchmark workflow
  benchmark_protocol.md         ED/VMC/replay audit protocol
  public_audit_snapshot.md      small public snapshot of the audit table
  technical_note.md             application-facing technical note
  research_roadmap.md           near-term research plan and open questions
  application_project_summary.md Chinese application-ready project description
data/
  public_audit_snapshot.csv     small sanitized audit snapshot
scripts/
  summarize_public_snapshot.py  reproduce docs/generated_public_report.md
src/haldane_nqs_public/
  observables.py                lightweight public observable helpers
examples/
  observable_demo.py            minimal observable convention demo
```

Quick local checks:

```bash
PYTHONPATH=src python examples/observable_demo.py
python scripts/summarize_public_snapshot.py
```

## 6. Claim Boundary

Safe public claim:

> This project built and organized a multi-observable NQS/VMC benchmark workflow for the interacting Haldane model, emphasizing that energy alone is not enough near competing topological and charge-ordered phases.

Not claimed here:

- a final thermodynamic phase diagram;
- complete many-body Chern closure for all interacting regimes;
- superiority over DMRG/QMC/iPEPS;
- raw unpublished numerical tables or checkpoints.

## 7. Application Summary

This is my most complete research project so far. It trained me to connect physics modeling, NQS ansatz design, exact benchmark construction, VMC computation, topology/order diagnostics, and reproducible scientific workflow.

## 8. Notes for Prospective Advisors

The most useful entry points are:

- [technical note](docs/technical_note.md): a human-readable summary of the problem, the audit contract, and the current claim boundary;
- [public audit snapshot](docs/public_audit_snapshot.md): a small, source-backed subset of the internal audit style, with sensitive paths and unpublished run trees removed;
- [generated public report](docs/generated_public_report.md): output reproduced from `data/public_audit_snapshot.csv`;
- [research roadmap](docs/research_roadmap.md): what I would do next if continuing this line;
- [model and observables](docs/model_and_observables.md): definitions of `Q`, `CDW`, and `Q2`;
- [benchmark protocol](docs/benchmark_protocol.md): how ED, training-best values, and strict replay are separated.

The private workspace contains more experiments than this public repository. I keep the public version deliberately conservative: it is meant to show what I did and how I think, not to publish an unfinished phase diagram.
