# NQS/VMC Methodology

## Why NQS?

Neural Quantum States parameterize many-body wavefunctions with trainable neural networks. In this project, NQS is used as a variational ansatz for a strongly correlated topological lattice model.

The project is not about adding a neural network for its own sake. It asks which wavefunction structures help represent:

- Chern-insulator branches;
- CDW branches;
- near-degenerate competing states;
- topology/order mismatch;
- finite-size fluctuation baselines.

## Ansatz Families

The private research workspace explored several families:

1. Slater-Jastrow baseline.
2. Neural backflow corrections.
3. Orbital-mixing references.
4. Multi-reference CI/CDW branches.
5. Source-free direct Hamiltonian learning on ED-sized Hilbert spaces.
6. GNN-style size transfer / teacher bias transfer.

This public repository does not publish the full private code or result tables. It documents the structure and scientific reasoning behind the project.

## Strict Replay

Training-best checkpoints can be optimistic. A report-grade checkpoint should be reloaded, evaluated with fresh walkers / independent replay, and compared against the same observable set. This is the strict replay idea:

```text
train -> select checkpoint -> reload -> fresh evaluation -> source-backed table
```

Strict replay is especially important near first-order or multi-basin regimes, where a training trajectory can temporarily visit a good-looking basin without producing a stable variational state.

