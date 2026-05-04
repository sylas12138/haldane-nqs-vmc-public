"""Minimal demo for public observable conventions."""

from __future__ import annotations

import numpy as np

from haldane_nqs_public import cdw_amplitude, q2_amplitude


def main() -> None:
    n_sites = 18
    n_a = np.array([4, 5, 6, 5, 7])
    n_b = np.array([5, 4, 3, 4, 2])
    print(f"CDW=<|Q|>: {cdw_amplitude(n_a, n_b, n_sites):.6f}")
    print(f"Q2=<Q^2>: {q2_amplitude(n_a, n_b, n_sites):.6f}")


if __name__ == "__main__":
    main()

