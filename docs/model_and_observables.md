# Model and Observables

## Interacting Haldane Model

The model is a spinless fermion Hamiltonian on a honeycomb lattice. The noninteracting Haldane hopping produces a Chern-insulator band structure, while nearest-neighbor repulsion favors charge-density-wave order.

```text
H = H_t1 + H_t2(phi) + H_V
```

where:

- `H_t1`: nearest-neighbor hopping;
- `H_t2(phi)`: complex next-nearest-neighbor Haldane hopping;
- `H_V`: nearest-neighbor density-density repulsion.

The benchmark focuses on the near-critical region where Chern-insulator and CDW-like branches compete.

## Sublattice Imbalance

Let `N_A` and `N_B` be particle numbers on the two honeycomb sublattices, and let `N` be the total number of sites. At half filling:

```text
Q = (N_A - N_B) / (N / 2)
CDW = <|Q|>
Q2 = <Q^2>
```

These are amplitude diagnostics. They differ from the signed order parameter:

```text
<N_A - N_B>
```

In finite systems, an A/B-symmetric state can satisfy `<N_A-N_B>=0` while still having nonzero `<|Q|>` and `<Q^2>`. This is why CDW/Q2 must be interpreted relative to the finite-size fluctuation baseline.

## Diagnostic Set

A candidate NQS/VMC result is not evaluated by energy alone. The diagnostic set includes:

- `E/N`: energy per site;
- `CDW`: first absolute moment of sublattice imbalance;
- `Q2`: second moment of sublattice imbalance;
- topology diagnostic;
- local-energy variance;
- strict replay stability.

