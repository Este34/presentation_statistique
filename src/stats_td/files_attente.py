"""Sujet 4 : processus de Poisson, loi de Poisson et file d'attente M/M/1.

Tout l'aléa passe par un ``rng`` (``np.random.Generator``) reçu en argument.
Convention : L_n = nombre de clients présents (en attente + en service) juste
avant l'arrivée du n-ième client ; la file est vide à t = 0, donc L_1 = 0.
"""

import numpy as np


def _expo(lam, rng):
    """Un tirage de E(lam) par inversion : -ln(1 - U) / lam (1 - U évite ln 0)."""
    return -np.log(1.0 - rng.random()) / lam


def nombre_points_poisson(lam, duree, rng):
    """Nombre de points d'un processus de Poisson d'intensité lam dans [0, duree].

    On additionne des durées E(lam) tant que la somme Z_i reste <= duree :
    N = sum_i 1{Z_i <= duree}, de loi P(lam * duree) (sujet 4, B.3 et
    simulation Q2). Coût moyen : lam * duree + 1 uniformes.
    """
    if lam <= 0:
        raise ValueError("lambda doit être strictement positif")
    if duree < 0:
        raise ValueError("la durée doit être positive")
    n = 0
    Z = _expo(lam, rng)
    while Z <= duree:
        n += 1
        Z += _expo(lam, rng)
    return n


def poisson_comptage(lam, T, rng, duree=1.0):
    """T tirages indépendants de P(lam * duree) par comptage d'exponentielles.

    Avec duree = 1 : algorithme de l'énoncé, N = sum_{i>=1} 1{Z_i <= 1}.
    """
    return np.array([nombre_points_poisson(lam, duree, rng) for _ in range(T)], dtype=np.int64)


def file_mm1(lam, mu, duree, rng):
    """File M/M/1 simulée par la récurrence L_{n+1} = max(0, L_n + 1 - A_n).

    - écart entre deux arrivées s = T_{n+1} - T_n ~ E(lam) (inversion) ;
    - A_n = nombre de services potentiels pendant s ~ P(mu * s) (comptage
      d'exponentielles E(mu)) ;
    - la file est vide à t = 0 : L_1 = 0.
    Renvoie (T, L) : instants d'arrivée dans [0, duree] et longueur juste avant
    chaque arrivée.
    """
    if lam <= 0 or mu <= 0:
        raise ValueError("lambda et mu doivent être strictement positifs")
    T, L = [], []
    t, l = _expo(lam, rng), 0  # T_1 et L_1 = 0
    while t <= duree:
        T.append(t)
        L.append(l)
        s = _expo(lam, rng)                      # T_{n+1} - T_n
        A = nombre_points_poisson(mu, s, rng)    # services potentiels sur [T_n, T_{n+1}[
        l = max(0, l + 1 - A)                    # récurrence (Q1)
        t += s
    return np.array(T), np.array(L, dtype=np.int64)


def longueur_recurrence(A):
    """L_1 = 0 et L_{n+1} = max(0, L_n + 1 - A_n), calculé pas à pas."""
    L = np.zeros(len(A) + 1, dtype=np.int64)
    for n, a in enumerate(A):
        L[n + 1] = max(0, L[n] + 1 - a)
    return L


def longueur_lindley(A):
    """Même suite par la formule de Lindley : L_n = S_n - min_{k<=n} S_k.

    S_1 = 0 et S_n = sum_{k<n} (1 - A_k). Vectorisé (cumsum, minimum cumulé).
    """
    S = np.concatenate([[0], np.cumsum(1 - np.asarray(A, dtype=np.int64))])
    return S - np.minimum.accumulate(S)


def _instants_poisson(lam, duree, rng):
    """Instants d'un processus de Poisson d'intensité lam dans [0, duree] (cumsum de E(lam))."""
    morceaux, t = [], 0.0
    taille = int(lam * duree + 10 * np.sqrt(lam * duree + 1)) + 10
    while t <= duree:
        Z = t + np.cumsum(-np.log(1.0 - rng.random(taille)) / lam)
        morceaux.append(Z)
        t = Z[-1]
    Z = np.concatenate(morceaux)
    return Z[Z <= duree]


def file_mm1_vectorisee(lam, mu, duree, rng):
    """Même modèle, vectorisé : on tire d'un coup les arrivées (intensité lam) et les
    services potentiels N(t) (intensité mu) sur [0, duree], puis
    A_n = N(T_{n+1}) - N(T_n) par np.searchsorted, et L par la formule de Lindley.

    Renvoie (T, L, A).
    """
    if lam <= 0 or mu <= 0:
        raise ValueError("lambda et mu doivent être strictement positifs")
    T = _instants_poisson(lam, duree, rng)
    S = _instants_poisson(mu, duree, rng)
    A = np.diff(np.searchsorted(S, T))  # points de N entre deux arrivées
    return T, longueur_lindley(A), A


def file_mm1_evenements(lam, mu, n_clients, rng):
    """Simulation directe, indépendante de la récurrence (validation).

    Chaque client a son propre service E(mu) ; serveur unique FIFO :
    départ D_n = max(T_n, D_{n-1}) + service_n. Le client n trouve devant lui
    les clients k < n pas encore partis : L_n = #{k < n : D_k > T_n}.
    """
    T = np.cumsum(-np.log(1.0 - rng.random(n_clients)) / lam)
    service = -np.log(1.0 - rng.random(n_clients)) / mu
    D = np.empty(n_clients)
    fin = 0.0
    for n in range(n_clients):
        fin = max(T[n], fin) + service[n]
        D[n] = fin
    # D est croissant (FIFO) : D_k <= T_n n'arrive que pour k < n
    L = np.arange(n_clients) - np.searchsorted(D, T, side="right")
    return T, L


def loi_stationnaire(rho, k):
    """P(L = k) = (1 - rho) rho^k (rho = lam / mu < 1)."""
    if not 0 <= rho < 1:
        raise ValueError("il faut 0 <= rho < 1 pour une loi stationnaire")
    k = np.asarray(k)
    return (1 - rho) * rho**k


def indicateurs_theoriques(rho):
    """Formules analytiques de la loi géométrique (1 - rho) rho^k."""
    if not 0 <= rho < 1:
        raise ValueError("il faut 0 <= rho < 1")
    return {
        "moyenne": rho / (1 - rho),
        "variance": rho / (1 - rho) ** 2,
        "p_serveur_libre": 1 - rho,
        "p_plus_de_5": rho**6,
    }


def moyenne_par_lots(x, n_lots=30):
    """Moyenne et erreur-type par la méthode des lots (batch means).

    Les valeurs successives sont corrélées : on coupe la série en n_lots blocs
    contigus, on moyenne chaque bloc, et on traite ces moyennes comme à peu près
    indépendantes : erreur-type = écart-type des moyennes / sqrt(n_lots) (ddof=1).
    """
    x = np.asarray(x, dtype=float)
    taille = len(x) // n_lots
    if taille < 1:
        raise ValueError("trop de lots pour la longueur de la série")
    lots = x[: taille * n_lots].reshape(n_lots, taille).mean(axis=1)
    return lots.mean(), lots.std(ddof=1) / np.sqrt(n_lots)
