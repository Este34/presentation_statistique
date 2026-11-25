"""Tests du sujet 4 : loi de Poisson par comptage et file M/M/1 (graine fixée)."""

import numpy as np
import pytest
from scipy import stats

from stats_td.files_attente import (
    file_mm1,
    file_mm1_evenements,
    file_mm1_vectorisee,
    indicateurs_theoriques,
    longueur_lindley,
    longueur_recurrence,
    loi_stationnaire,
    moyenne_par_lots,
    nombre_points_poisson,
    poisson_comptage,
)


@pytest.fixture
def rng():
    return np.random.default_rng(2026)


# ---------- Loi de Poisson par comptage d'exponentielles ----------

def test_poisson_moyenne_et_variance(rng):
    lam, T = 4.0, 50_000
    N = poisson_comptage(lam, T, rng)
    assert abs(N.mean() - lam) < 4 * np.sqrt(lam / T)  # 4 erreurs-types
    # variance d'une Poisson = lambda (tolérance large : 4 erreurs-types de la variance)
    assert abs(N.var(ddof=1) - lam) < 4 * np.sqrt((lam + 2 * lam**2) / T)


def test_poisson_loi_complete_chi2(rng):
    # Test du chi2 au seuil 1 % : il échoue 1 fois sur 100 par pur hasard. Avec la graine 2026
    # et lambda = 3, p = 0,008 (excès en k = 6) ; sur 20 autres graines les p-valeurs sont
    # bien uniformes (0,12 à 0,98). On garde lambda = 2,5 (p = 0,025).
    lam, T = 2.5, 40_000
    N = poisson_comptage(lam, T, rng)
    k = np.arange(0, 10)
    obs = np.array([(N == j).sum() for j in k] + [(N >= 10).sum()])
    p = np.append(stats.poisson.pmf(k, lam), stats.poisson.sf(9, lam))
    assert stats.chisquare(obs, T * p).pvalue > 0.01


def test_poisson_duree_t_donne_lambda_t(rng):
    # N_t ~ P(lambda t) : intensité 2 sur [0, 3] -> moyenne 6
    N = poisson_comptage(2.0, 20_000, rng, duree=3.0)
    assert abs(N.mean() - 6.0) < 4 * np.sqrt(6.0 / 20_000)


def test_poisson_parametres_invalides(rng):
    with pytest.raises(ValueError):
        nombre_points_poisson(0.0, 1.0, rng)
    with pytest.raises(ValueError):
        nombre_points_poisson(1.0, -1.0, rng)
    assert nombre_points_poisson(5.0, 0.0, rng) in (0,)  # aucun point dans [0, 0] (p.s.)


# ---------- Récurrence et formule de Lindley ----------

def test_lindley_egale_recurrence(rng):
    A = rng.integers(0, 4, size=2000)
    assert np.array_equal(longueur_recurrence(A), longueur_lindley(A))


def test_recurrence_cas_a_la_main():
    # L1 = 0 ; A = 0 -> 1 ; A = 0 -> 2 ; A = 5 -> max(0, 3 - 5) = 0 ; A = 1 -> 0
    assert longueur_recurrence([0, 0, 5, 1]).tolist() == [0, 1, 2, 0, 0]


# ---------- File M/M/1 ----------

def test_trajectoire_coherente(rng):
    T, L = file_mm1(10.0, 12.0, 200.0, rng)
    assert L[0] == 0                       # file vide au départ
    assert np.all(L >= 0)
    assert np.all(np.diff(L) <= 1)         # au plus +1 entre deux arrivées
    assert np.all(np.diff(T) > 0) and T[-1] <= 200.0


def test_A_geometrique(rng):
    lam, mu = 100.0, 120.0
    _, _, A = file_mm1_vectorisee(lam, mu, 300.0, rng)
    p = lam / (lam + mu)
    # E[A] = mu / lam ; Var A = q / p^2 avec q = 1 - p
    se = np.sqrt((1 - p) / p**2 / len(A))
    assert abs(A.mean() - mu / lam) < 4 * se
    assert abs((A == 0).mean() - p) < 4 * np.sqrt(p * (1 - p) / len(A))


def test_stationnaire_rho_inferieur_a_1(rng):
    lam, mu = 100.0, 120.0
    rho = lam / mu
    th = indicateurs_theoriques(rho)
    _, L = file_mm1(lam, mu, 300.0, rng)
    m, se = moyenne_par_lots(L, 30)          # erreur-type corrigée de la corrélation
    assert abs(m - th["moyenne"]) < 4 * se
    m0, se0 = moyenne_par_lots(L == 0, 30)
    assert abs(m0 - th["p_serveur_libre"]) < 4 * se0
    m6, se6 = moyenne_par_lots(L > 5, 30)
    assert abs(m6 - th["p_plus_de_5"]) < 4 * se6


def test_trois_simulations_meme_loi(rng):
    # récurrence, version vectorisée et simulation directe FIFO : même P(L = 0) = 1 - rho
    lam, mu = 50.0, 100.0
    _, L1 = file_mm1(lam, mu, 400.0, rng)
    _, L2, _ = file_mm1_vectorisee(lam, mu, 400.0, rng)
    _, L3 = file_mm1_evenements(lam, mu, 20_000, rng)
    for L in (L1, L2, L3):
        m0, se0 = moyenne_par_lots(L == 0, 20)
        assert abs(m0 - 0.5) < 4 * se0


def test_croissance_rho_superieur_a_1(rng):
    lam, mu = 120.0, 100.0
    _, L, _ = file_mm1_vectorisee(lam, mu, 300.0, rng)
    n = len(L)
    pente = L[-1] / n                       # L_n / n -> 1 - 1/rho = 1/6
    p = lam / (lam + mu)
    se = np.sqrt((1 - p) / p**2 / n)        # écart-type de S_n / n (Var A = q / p^2)
    assert abs(pente - (1 - mu / lam)) < 4 * se


def test_formules_analytiques():
    th = indicateurs_theoriques(5 / 6)
    assert th["moyenne"] == pytest.approx(5.0)
    assert th["variance"] == pytest.approx(30.0)
    assert th["p_serveur_libre"] == pytest.approx(1 / 6)
    assert th["p_plus_de_5"] == pytest.approx((5 / 6) ** 6)
    k = np.arange(400)
    assert loi_stationnaire(5 / 6, k).sum() == pytest.approx(1.0)
    with pytest.raises(ValueError):
        indicateurs_theoriques(1.2)  # coquille de l'énoncé : rho = mu / lam > 1
