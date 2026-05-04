# Technical Note: Interacting Haldane NQS/VMC Benchmark

## 1. What This Project Is About

This project studies the interacting spinless-fermion Haldane model with neural quantum states and variational Monte Carlo.

The physical problem is clean but not easy. At small nearest-neighbor repulsion `V`, the system is a Chern insulator. At large `V`, it favors a charge-density-wave state that breaks the A/B sublattice balance. Near the transition, several variational branches can be close in energy. A wavefunction can therefore look good by energy while still carrying the wrong order or topology.

That is the main reason I used this model as a benchmark. It is not just a place to run a neural network. It is a place to ask whether a neural wavefunction is actually learning the right physics.

## 2. Model

The model is the honeycomb-lattice Haldane Hamiltonian with nearest-neighbor repulsion:

```text
H = -t1 sum_<ij> (c_i^dagger c_j + h.c.)
    -t2 sum_<<ij>> (exp(i phi nu_ij) c_i^dagger c_j + h.c.)
    +V sum_<ij> n_i n_j
```

The benchmark is usually set at half filling on finite clusters. Small clusters can be compared with exact diagonalization. Larger clusters require internal VMC audits.

## 3. Order Diagnostics

For half filling, I use the A/B sublattice imbalance

```text
Q = (N_A - N_B) / (N / 2)
```

and report

```text
CDW = <|Q|>
Q2  = <Q^2>
```

This convention matters. `CDW` and `Q2` are finite-size, symmetry-even amplitude diagnostics. They are not the signed order parameter `<N_A-N_B>`. A finite cluster can have nonzero `CDW` and `Q2` even on the Chern-insulator side because the diagnostics measure fluctuation amplitude.

So I do not read a nonzero `CDW` value alone as proof of charge order. I compare it against ED, energy, topology, and replay stability.

## 4. Ansatz Families

The private research workspace explored several ansatz ideas:

- Slater-Jastrow baselines;
- neural backflow;
- orbital mixing;
- branch-conditioned references;
- multi-reference CI/CDW branches;
- source-free direct Hamiltonian learning on ED-sized systems;
- GNN-style transfer between sizes;
- strict replay using fresh samples.

I do not treat a larger network as automatically better. Near a first-order or near-critical competition, adding capacity can simply make the optimizer better at finding a biased branch. That is why the project compares ansatz families through an audit contract, not only through best training energy.

## 5. Audit Contract

The internal workflow separates:

- training-best energy;
- strict replay energy;
- `CDW` and `Q2`;
- topology diagnostic;
- variance or local-energy stability;
- source provenance;
- pass/fail reason.

This separation is important because training-best values are often optimistic. A checkpoint can be selected from a favorable sampler state, but fresh replay may move the energy or observables. I regard strict replay as the more honest value for external reporting.

## 6. Topology Diagnostic Boundary

Topology is the most delicate part of this project. In the public materials I avoid calling every one-body diagnostic a many-body Chern number.

The useful hierarchy is:

1. one-body / Green-projector style diagnostics;
2. twist or boundary-condition diagnostics for NQS;
3. ED subspace or Wilson-loop style checks on small clusters;
4. many-body topology statements, only when the audit really supports them.

This is conservative, but it is the right convention. It prevents a visually convincing plot from becoming an unsupported topological claim.

## 7. What I Learned

The strongest lesson is that NQS/VMC near competing phases is not just an optimization problem. It is also a scientific-audit problem.

Energy is necessary, but not sufficient. A useful result must answer:

- Is the energy close to ED or a trusted baseline?
- Does the order parameter match the expected branch?
- Does the topology diagnostic agree with the claimed phase?
- Does fresh replay reproduce the training-selected checkpoint?
- Is the result robust to ansatz family and initialization?

This is the same habit I now want to carry into broader AI for Science work: AI should accelerate scientific computation, but the human workflow still needs benchmark, provenance, and failure analysis.

## 8. Public Result Boundary

The public repository shows the model, observables, benchmark protocol, and a small audit snapshot. It does not release raw checkpoints, full result trees, remote job scripts, private failure logs, or unpublished detailed tables.

The safe conclusion is:

> This project built a conservative multi-observable benchmark workflow for interacting Haldane NQS/VMC calculations near competing Chern-insulator and charge-ordered branches.

The current public release does not claim a final thermodynamic phase diagram.
