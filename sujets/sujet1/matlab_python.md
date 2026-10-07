# Correspondances Matlab → Python (Sujet 1)

| Besoin (énoncé) | Matlab | Python (numpy / matplotlib) | Piège |
|---|---|---|---|
| Uniforme sur [0,1] | `rand(1,T)` | `rng = np.random.default_rng(graine)` puis `rng.random(T)` | Tirage dans `[0,1)` : `0` possible, donc `log(1-U)` |
| Gaussienne de référence | `randn(1,T)` | `rng.standard_normal(T)` | Sert uniquement à vérifier Box-Muller |
| Moyenne | `mean(Y)` | `Y.mean()` | — |
| Variance | `cov(Y)` ou `var(Y)` | `Y.var(ddof=1)` | Par défaut, numpy divise par `T` (`ddof=0`) ; Matlab divise par `T-1` |
| Écart-type | `std(Y)` | `Y.std(ddof=1)` | Même remarque |
| Histogramme | `hist(Y, n)` | `np.histogram(Y, bins=n)` ou `plt.hist(Y, bins=n, density=True)` | `density=True` pour comparer à une densité |
| F estimée | `cumsum(hist(Y,n))/T` | `np.cumsum(effectifs) / T` | Donne F aux bords **droits** des classes |
| Semi-log | `semilogy(x, y)` | `plt.semilogy(x, y)` ou `ax.set_yscale("log")` | `log(0)` : ne pas tracer F^c = 0 |
| Lire un point sur la figure | `ginput(2)` | remplacé par `np.polyfit(y, np.log(Fc), 1)` | Régression = plus précis et reproductible qu'un clic |
| Graine | `rng(2026)` | `np.random.default_rng(2026)` | Fixer la graine rend les résultats reproductibles |

Le code réutilisable est dans `src/stats_td/` (`generateurs.py`, `empirique.py`).
