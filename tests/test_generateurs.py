"""Tests statistiques des générateurs (graine fixée → déterministes)."""

import numpy as np
import pytest
from scipy import stats

from stats_td.empirique import (
    pente_semilog,
    repartition_complementaire,
    repartition_empirique,
    repartition_histogramme,
)
from stats_td.generateurs import box_muller, exponentielle_inversion, gaussienne

T = 10_000
LAM = 2.0


@pytest.fixture
def rng():
    return np.random.default_rng(2026)


def test_exponentielle_moyenne_variance(rng):
    Y = exponentielle_inversion(LAM, T, rng)
    # erreur-type de la moyenne : sigma / sqrt(T) = (1/lam) / 100
    assert abs(Y.mean() - 1 / LAM) < 4 * (1 / LAM) / np.sqrt(T)
    assert abs(Y.var(ddof=1) - 1 / LAM**2) < 0.02
    assert Y.min() >= 0


def test_exponentielle_ks(rng):
    Y = exponentielle_inversion(LAM, T, rng)
    assert stats.kstest(Y, "expon", args=(0, 1 / LAM)).pvalue > 0.01


def test_exponentielle_lambda_invalide(rng):
    with pytest.raises(ValueError):
        exponentielle_inversion(-1, 10, rng)


def test_pente_semilog(rng):
    pente, ordonnee = pente_semilog(exponentielle_inversion(LAM, T, rng))
    assert pente == pytest.approx(-LAM, rel=0.05)
    assert ordonnee == pytest.approx(0, abs=0.05)  # F^c(0) = 1 → ln = 0


def test_box_muller_normales_independantes(rng):
    X1, X2 = box_muller(T, rng)
    for X in (X1, X2):
        assert stats.kstest(X, "norm").pvalue > 0.01
    assert abs(np.corrcoef(X1, X2)[0, 1]) < 4 / np.sqrt(T)
    # r² = X1² + X2² ~ E(1/2), donc de moyenne 2
    assert stats.kstest(X1**2 + X2**2, "expon", args=(0, 2)).pvalue > 0.01


def test_gaussienne_mu_sigma2(rng):
    Y = gaussienne(5, 4, T, rng)
    assert len(Y) == T
    assert abs(Y.mean() - 5) < 4 * 2 / np.sqrt(T)
    assert Y.var(ddof=1) == pytest.approx(4, rel=0.06)
    assert stats.kstest(Y, stats.norm(loc=5, scale=2).cdf).pvalue > 0.01


def test_gaussienne_taille_impaire(rng):
    assert len(gaussienne(0, 1, 7, rng)) == 7


def test_repartitions_coherentes(rng):
    Y = exponentielle_inversion(LAM, 1000, rng)
    y, F = repartition_empirique(Y)
    _, Fc = repartition_complementaire(Y)
    assert F[-1] == 1 and Fc[0] == 1
    # F_n(y_i) + F^c_n(y_i) = 1 + 1/n (le point y_i est compté deux fois)
    assert np.allclose(F + Fc, 1 + 1 / len(Y))
    _, Fh = repartition_histogramme(Y)
    assert Fh[-1] == pytest.approx(1)
    assert np.all(np.diff(Fh) >= 0)
