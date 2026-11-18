# Correspondances Matlab → Python (Sujet 3)

| Besoin (énoncé) | Matlab | Python (numpy / matplotlib) | Piège |
|---|---|---|---|
| Discrétiser $[-8\pi, 8\pi]$ | `y = linspace(-8*pi, 8*pi, 5000)` | `y = np.linspace(-8*np.pi, 8*np.pi, 5000)` | La formule $\frac{n-1}{5000}$ de l'énoncé n'atteint pas $8\pi$ |
| Évaluer $h$ sur la grille | `h = y.^2 + 3*y.*cos(y)` (opérations **pointées**) | `h = y**2 + 3*y*np.cos(y)` | En Matlab, oublier le `.` fait un produit matriciel |
| Boucle | `for n = 1:N ... end` | `for n in range(1, N + 1):` | Indices à partir de 1 en Matlab, de 0 en Python |
| Uniforme sur $[0,1]$ | `rand` | `rng.random()` (`rng = np.random.default_rng(2026)`) | — |
| Uniforme sur $[x - \pi/2, x + \pi/2]$ | `x - pi/2 + pi*rand` | `rng.uniform(x - np.pi/2, x + np.pi/2)` | Largeur totale $\pi$, pas $\pi/2$ |
| Accepter avec probabilité $p$ | `if rand < exp(-dh/T)` | `if rng.random() < np.exp(-dh / T):` | $P(U < p) = p$ |
| Minimum d'un vecteur et sa position | `[m, i] = min(h)` | `i = np.argmin(h); m = h[i]` | `min` Matlab renvoie aussi l'indice |
| Maximum | `max(h)` | `h.max()` | — |
| Tracer, superposer | `plot(y, h); hold on; plot(x, h(x), 'o'); hold off` | `ax.plot(y, h); ax.plot(x, h_x, "o")` | En matplotlib, tracer sur le même `ax` superpose (pas de `hold`) |
| Graine | `rng(2026)` | `np.random.default_rng(2026)` | Les deux générateurs ne donnent pas les mêmes tirages |

Le code réutilisable est dans `src/stats_td/optimisation.py` (`gradient_simple`,
`recuit_simule`, `h_sujet3`, `dh_sujet3`).
