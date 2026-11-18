"""Tests du sujet 3 : gradient simple et recuit simulé (graine fixée)."""

import numpy as np
import pytest
from scipy.optimize import brentq

from stats_td.optimisation import (
    BORNES_SUJET3,
    dh_sujet3,
    gradient_simple,
    h_sujet3,
    minima_locaux,
    recuit_simule,
)

X_GLOBAL = brentq(dh_sujet3, -1.0, 0.0)  # h'(x) = 0 près de -0,64
X_LOCAL_75 = brentq(dh_sujet3, 8.0, 9.5)  # minimum local du bassin de x0 = 7,5


@pytest.fixture
def rng():
    return np.random.default_rng(2026)


def test_derivee_par_differences_finies():
    x = np.linspace(-20, 20, 101)
    eps = 1e-6
    approx = (h_sujet3(x + eps) - h_sujet3(x - eps)) / (2 * eps)
    assert np.allclose(dh_sujet3(x), approx, atol=1e-5)


def test_minimum_global_sur_l_intervalle():
    xm, hm = minima_locaux(h_sujet3, *BORNES_SUJET3)
    assert len(xm) == 9
    assert xm[np.argmin(hm)] == pytest.approx(X_GLOBAL, abs=1e-3)
    # le minimum global intérieur est plus bas que les valeurs aux bords
    assert hm.min() < min(h_sujet3(np.array(BORNES_SUJET3)))


def test_gradient_reste_dans_le_bassin_local():
    x = gradient_simple(dh_sujet3, 7.5, 1000)
    assert 7.5 < x[-1] < X_LOCAL_75  # monte vers 8,81 sans le dépasser
    assert np.all(np.diff(h_sujet3(x)) <= 1e-12)  # h décroît à chaque pas
    # convergence lente en n^(-c) : il reste encore un écart après 1000 itérations
    assert 0.05 < X_LOCAL_75 - x[-1] < 0.3


def test_gradient_deterministe():
    assert np.array_equal(gradient_simple(dh_sujet3, 7.5, 50), gradient_simple(dh_sujet3, 7.5, 50))


def test_gradient_n_invalide():
    with pytest.raises(ValueError):
        gradient_simple(dh_sujet3, 7.5, 0)


def test_recuit_reste_dans_les_bornes(rng):
    x, _ = recuit_simule(h_sujet3, 7.5, 1000, rng, bornes=BORNES_SUJET3)
    assert np.all((x >= BORNES_SUJET3[0]) & (x <= BORNES_SUJET3[1]))


def test_recuit_accepte_beaucoup_au_debut_peu_a_la_fin(rng):
    _, acc = recuit_simule(h_sujet3, 7.5, 1000, rng, bornes=BORNES_SUJET3)
    assert acc[:100].mean() > 0.7
    assert acc[-100:].mean() < 0.3


def test_recuit_atteint_souvent_le_minimum_global():
    # 200 lancers indépendants : proportion de succès p, erreur-type <= 0,5/sqrt(200)
    rng = np.random.default_rng(2026)
    fins = np.array(
        [recuit_simule(h_sujet3, 7.5, 1000, rng, bornes=BORNES_SUJET3)[0][-1] for _ in range(200)]
    )
    succes = np.mean(np.abs(fins - X_GLOBAL) < 0.5)  # même critère que le notebook
    assert succes > 0.5  # largement mieux que le gradient (0 %)


def test_recuit_parametres_invalides(rng):
    with pytest.raises(ValueError):
        recuit_simule(h_sujet3, 7.5, 10, rng, alpha=1.0)


def test_recuit_regle_acceptation():
    # T immense : toute proposition dans les bornes est acceptée (e^{-delta/T} ~ 1)
    _, acc = recuit_simule(h_sujet3, 0.0, 200, np.random.default_rng(1), T0=1e12, alpha=0.999999)
    assert acc.all()
    # T minuscule : on n'accepte que des descentes, donc h ne remonte jamais
    x, _ = recuit_simule(h_sujet3, 7.5, 500, np.random.default_rng(1), T0=1e-12, alpha=0.5)
    assert np.all(np.diff(h_sujet3(x)) <= 0)


def test_recuit_refuse_hors_bornes_pres_du_bord():
    x0 = BORNES_SUJET3[1] - 0.1
    x, _ = recuit_simule(h_sujet3, x0, 300, np.random.default_rng(3), T0=1e12, alpha=0.999999,
                         bornes=BORNES_SUJET3)
    assert np.all(x <= BORNES_SUJET3[1])


def test_recuit_x0_hors_bornes(rng):
    with pytest.raises(ValueError):
        recuit_simule(h_sujet3, 100.0, 10, rng, bornes=BORNES_SUJET3)
