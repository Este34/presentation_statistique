"""Générateurs de variables aléatoires à partir de U ~ U[0, 1].

Chaque fonction prend un ``rng`` (``np.random.Generator``) pour que les
résultats soient reproductibles (graine fixée dans les notebooks et les tests).
"""

import numpy as np


def uniforme(T, rng):
    """T tirages de U[0, 1) — équivalent de ``rand(1, T)`` en Matlab."""
    return rng.random(T)


def exponentielle_inversion(lam, T, rng):
    """Loi E(lam) par inversion : Y = F^{-1}(U) = -ln(1 - U) / lam.

    On utilise 1 - U (dans ]0, 1]) plutôt que U (dans [0, 1)) pour ne
    jamais calculer ln(0). Comme 1 - U suit aussi U[0, 1], -ln(U)/lam
    donnerait la même loi.
    """
    if lam <= 0:
        raise ValueError("lambda doit être strictement positif")
    U = uniforme(T, rng)
    return -np.log(1.0 - U) / lam


def box_muller(T, rng):
    """Deux échantillons indépendants de N(0, 1) par Box-Muller.

    r² = -2 ln(U1) ~ E(1/2) (inversion) et theta = 2 pi U2 ~ U[0, 2pi],
    puis retour en cartésiennes : X1 = r cos(theta), X2 = r sin(theta).
    """
    U1 = 1.0 - uniforme(T, rng)  # dans ]0, 1] : évite ln(0)
    U2 = uniforme(T, rng)
    r = np.sqrt(-2.0 * np.log(U1))
    theta = 2.0 * np.pi * U2
    return r * np.cos(theta), r * np.sin(theta)


def gaussienne(mu, sigma2, T, rng):
    """T réalisations de N(mu, sigma2) : Y = mu + sigma * X avec X ~ N(0, 1).

    Attention : le paramètre est la VARIANCE sigma2, on multiplie par
    l'écart-type sigma = sqrt(sigma2).
    """
    X1, X2 = box_muller((T + 1) // 2, rng)
    X = np.concatenate([X1, X2])[:T]  # Box-Muller donne 2 valeurs par tirage
    return mu + np.sqrt(sigma2) * X
