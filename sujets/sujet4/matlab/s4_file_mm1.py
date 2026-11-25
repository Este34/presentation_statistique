"""Sujet 4 en Python, ligne à ligne comme s4_file_mm1.m (générateur PCG64, graine 2026)."""
import numpy as np

rng = np.random.default_rng(2026)


def nb_points_poisson(lam, duree):
    # Nombre de points d'un processus de Poisson d'intensité lam dans [0, duree]
    n = 0
    Z = -np.log(1 - rng.random()) / lam   # inversion, 1 - U évite log(0)
    while Z <= duree:
        n += 1
        Z = Z - np.log(1 - rng.random()) / lam
    return n


# Simulation Q2 : P(4) en comptant les sommes d'exponentielles <= 1
T = 10000; N = np.zeros(T)
for i in range(T):
    N[i] = nb_points_poisson(4, 1)
print(f"P(4) : moyenne {N.mean():.4f}, variance {N.var(ddof=1):.4f}")

# Q2 et Q5 : file M/M/1, lambda = 100, mu = 120, 5 minutes, file vide au départ
lam, mu, duree = 100, 120, 300; rho = lam / mu
Ta = []; L = []
t = -np.log(1 - rng.random()) / lam; l = 0
while t <= duree:
    Ta.append(t); L.append(l)
    s = -np.log(1 - rng.random()) / lam   # T(n+1) - T(n), loi E(lambda)
    A = nb_points_poisson(mu, s)          # services potentiels, loi P(mu*s)
    l = max(0, l + 1 - A)                 # récurrence de la Q1
    t = t + s
Ta = np.array(Ta); L = np.array(L); n = len(L)
print(f"n = {n} clients, file max {L.max()}")
print(f"E[L]   = {L.mean():.4f} (théorie {rho / (1 - rho):.4f})")
print(f"Var L  = {L.var(ddof=1):.4f} (théorie {rho / (1 - rho)**2:.4f})")
print(f"P(L=0) = {np.mean(L == 0):.4f} (théorie {1 - rho:.4f})")
print(f"P(L>5) = {np.mean(L > 5):.4f} (théorie {rho**6:.4f})")
