# Research Roadmap

This roadmap explains what I would do next if I continued the interacting Haldane NQS/VMC line as a graduate research project.

## 1. Short-Term Goal

The immediate goal is not to claim a thermodynamic phase diagram. The goal is to make the ED-sized benchmark hard to fool.

That means:

- separate training-best values from strict replay values;
- keep energy, `CDW`, `Q2`, and topology diagnostics in one table;
- compare ansatz families under the same audit contract;
- document rejected rows instead of silently discarding them.

## 2. ED-Sized Closure

On `L=3`, the project should close three questions:

1. Which ansatz family gives the best energy/order/topology consistency near the CI/CDW boundary?
2. Which failures come from optimization basin selection rather than expressive capacity?
3. Which topology diagnostic can be safely reported for an interacting finite cluster?

This step should produce a compact benchmark table rather than a long list of runs.

## 3. Scaling Test

After the ED-sized table is stable, the next step is a cautious `L=6` scaling test.

The scaling test should not start by searching the whole phase diagram. It should carry a small set of validated ansatz families and replay rules from `L=3` to `L=6`, then ask whether the same physics survives.

The minimum report should include:

- energy per site;
- `CDW=<|Q|>`;
- `Q2=<Q^2>`;
- replay stability;
- topology diagnostic level;
- whether the row is a physics candidate or a method diagnostic.

## 4. Better Wave-Function Ideas

The ansatz direction I would explore next:

- branch-aware references without hard-coding the answer;
- neural backflow with controlled orbital mixing;
- symmetry-aware charge features;
- small-cluster exact-sum training before sampled VMC;
- teacher-bias transfer only when the source and target tasks are clearly labeled.

I would avoid simply increasing model size without a physics reason.

## 5. Broader Direction

The broader research direction is to turn NQS/VMC into an auditable AI4S method for quantum many-body problems.

The Haldane model is one benchmark. The same philosophy can extend to:

- triangular-lattice charge order;
- moire effective models;
- disordered bosonic systems;
- quantum chemistry benchmark problems;
- agent-assisted scientific computing.

The common standard is the same: a result should be useful because it is reproducible and physically interpretable, not only because it is numerically low.
