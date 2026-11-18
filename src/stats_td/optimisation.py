"""Sujet 3 : gradient simple (déterministe) et recuit simulé (stochastique).

Les deux algorithmes renvoient toute la trajectoire (x_0, ..., x_N) pour pouvoir
tracer la convergence sur le graphe de h.
"""

import numpy as np

BORNES_SUJET3 = (-8 * np.pi, 8 * np.pi)


def h_sujet3(x):
    """h(x) = x² + 3x cos(x), la fonction à minimiser sur [-8π, 8π]."""
    return x**2 + 3 * x * np.cos(x)


def dh_sujet3(x):
    """h'(x) = 2x + 3 cos(x) - 3x sin(x) (dérivée d'un produit pour 3x cos x)."""
    return 2 * x + 3 * np.cos(x) - 3 * x * np.sin(x)


def pas_sujet3(n):
    """Pas conseillé alpha_n = 0,025 / n : sum alpha_n = +inf, sum alpha_n² < +inf."""
    return 0.025 / n


def gradient_simple(grad, x0, N, pas=pas_sujet3):
    """x_n = x_{n-1} - alpha_n h'(x_{n-1}), pour n = 1, ..., N.

    (Numérotation qui évite alpha_0 = 0,025/0, non défini.)

    Déterministe : même x0, même trajectoire. Renvoie le tableau (x_0, ..., x_N).
    """
    if N < 1:
        raise ValueError("N doit être >= 1")
    x = np.empty(N + 1)
    x[0] = x0
    for n in range(1, N + 1):
        x[n] = x[n - 1] - pas(n) * grad(x[n - 1])
    return x


def recuit_simule(f, x0, N, rng, T0=500.0, alpha=0.99, demi_largeur=np.pi / 2, bornes=None):
    """Recuit simulé, températures T_n = T0 * alpha^n.

    À l'itération n : z ~ U[x_n - demi_largeur, x_n + demi_largeur] (loi g_n) ;
    si f(z) <= f(x_n) on accepte ; sinon on accepte avec la probabilité
    exp(-(f(z) - f(x_n)) / T_n) ; en cas de refus, x_{n+1} = x_n.
    Si ``bornes`` = (a, b) est donné, un z hors de [a, b] est refusé : on
    minimise sur l'intervalle, pas sur R.

    Renvoie (x, acceptes) : la trajectoire (x_0, ..., x_N) et un booléen par
    itération (True si z a été accepté).
    """
    if T0 <= 0 or not 0 < alpha < 1:
        raise ValueError("il faut T0 > 0 et 0 < alpha < 1")
    if N < 1:
        raise ValueError("N doit être >= 1")
    if bornes is not None and not bornes[0] <= x0 <= bornes[1]:
        raise ValueError("x0 doit être dans les bornes")
    x = np.empty(N + 1)
    x[0] = x0
    fx = f(x0)
    acceptes = np.zeros(N, dtype=bool)
    for n in range(1, N + 1):
        T = T0 * alpha**n
        z = x[n - 1] + rng.uniform(-demi_largeur, demi_largeur)
        # On tire toujours U pour garder le même nombre d'appels au générateur.
        u = rng.random()
        dedans = bornes is None or bornes[0] <= z <= bornes[1]
        if dedans:
            fz = f(z)
            delta = fz - fx
            if delta <= 0 or u < np.exp(-delta / T):
                x[n], fx = z, fz
                acceptes[n - 1] = True
                continue
        x[n] = x[n - 1]
    return x, acceptes


def minima_locaux(f, a, b, n_points=200_001):
    """Minima locaux de f sur [a, b] repérés sur une grille fine.

    Équivalent de min/max sur le vecteur h_n de l'énoncé, mais en cherchant les
    points plus bas que leurs deux voisins (bords exclus).
    """
    y = np.linspace(a, b, n_points)
    v = f(y)
    i = np.where((v[1:-1] < v[:-2]) & (v[1:-1] < v[2:]))[0] + 1
    return y[i], v[i]
