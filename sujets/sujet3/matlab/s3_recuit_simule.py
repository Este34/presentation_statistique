"""Sujet 3 en Python, ligne à ligne comme s3_recuit_simule.m (mêmes chiffres que le notebook)."""
import numpy as np
from scipy.optimize import brentq

h = lambda x: x**2 + 3 * x * np.cos(x)
dh = lambda x: 2 * x + 3 * np.cos(x) - 3 * x * np.sin(x)
a, b, N = -8 * np.pi, 8 * np.pi, 1000


def recuit(x0, N, T0, alpha, rng):
    x = np.zeros(N + 1); x[0] = x0; hx = h(x0)
    for n in range(1, N + 1):
        T = T0 * alpha**n
        z = x[n - 1] + rng.uniform(-np.pi / 2, np.pi / 2)  # loi instrumentale g_n
        u = rng.random()
        x[n] = x[n - 1]                                    # par défaut : z refusé
        if a <= z <= b:                                    # hors de [-8pi, 8pi] : refusé
            hz = h(z)
            if hz <= hx or u < np.exp(-(hz - hx) / T):
                x[n], hx = z, hz                           # z accepté
    return x


# Q1 : h sur 5000 points, minimum de la grille
y = np.linspace(a, b, 5000); hy = h(y)
i = np.argmin(hy)
xs = brentq(dh, -1, 0)                                     # minimum global exact
print(f"Q1 grille : h({y[i]:.4f}) = {hy[i]:.4f} ; x* = {xs:.4f}")

# Q2 : gradient simple, pas 0,025/n
xg = np.zeros(N + 1); xg[0] = 7.5
for n in range(1, N + 1):
    xg[n] = xg[n - 1] - 0.025 / n * dh(xg[n - 1])
print(f"Q2 gradient : x_N = {xg[-1]:.4f}, h = {h(xg[-1]):.4f}")

# Q3 : un recuit, T0 = 500, alpha = 0,99
rng = np.random.default_rng(2026)
xr = recuit(7.5, N, 500, 0.99, rng)
print(f"Q3 recuit : x_N = {xr[-1]:.4f}, h = {h(xr[-1]):.4f}")

# Q4 : 1000 recuits indépendants, proportion de succès
R = 1000
fins = np.array([recuit(7.5, N, 500, 0.99, rng)[-1] for _ in range(R)])
p = np.mean(np.abs(fins - xs) < 0.5); et = np.sqrt(p * (1 - p) / R)
print(f"Q4 : succès {p:.3f} +- {1.96 * et:.3f} (IC 95 %)")
