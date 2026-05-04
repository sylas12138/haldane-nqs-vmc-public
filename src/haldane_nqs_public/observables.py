"""Minimal public observable helpers for sublattice imbalance."""

from __future__ import annotations

import numpy as np


def imbalance_q(n_a: np.ndarray, n_b: np.ndarray, n_sites: int) -> np.ndarray:
    """Compute Q = (N_A - N_B) / (N / 2)."""
    if n_sites <= 0 or n_sites % 2:
        raise ValueError("n_sites must be a positive even integer")
    return (np.asarray(n_a, dtype=float) - np.asarray(n_b, dtype=float)) / (n_sites / 2)


def cdw_amplitude(n_a: np.ndarray, n_b: np.ndarray, n_sites: int) -> float:
    """Compute CDW = <|Q|>."""
    return float(np.mean(np.abs(imbalance_q(n_a, n_b, n_sites))))


def q2_amplitude(n_a: np.ndarray, n_b: np.ndarray, n_sites: int) -> float:
    """Compute Q2 = <Q^2>."""
    q = imbalance_q(n_a, n_b, n_sites)
    return float(np.mean(q * q))

