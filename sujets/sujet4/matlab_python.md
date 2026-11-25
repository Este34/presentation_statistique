# Correspondances Matlab → Python (Sujet 4)

| Besoin | Matlab | Python (numpy / matplotlib) | Piège |
|---|---|---|---|
| Uniforme sur $[0,1]$ | `rand` ; `rand(1, T)` | `rng.random()` ; `rng.random(T)` (`rng = np.random.default_rng(2026)`) | Valeurs dans $[0, 1[$ : $\ln 0$ possible |
| Exponentielle $\mathcal E(\lambda)$ | `-log(1 - rand) / lambda` | `-np.log(1 - rng.random()) / lam` | `log` = logarithme **népérien** dans les deux langages |
| Boucle conditionnelle | `while Z <= duree ... end` | `while Z <= duree:` |  |
| Compter les points de $[0, d]$ | `n = n + 1` dans la boucle | `n += 1` |  |
| Maximum de deux nombres | `max(0, l + 1 - A)` | `max(0, l + 1 - A)` | En numpy vectorisé : `np.maximum` |
| Sommes cumulées (instants $T_k$) | `cumsum(X)` | `np.cumsum(X)` |  |
| Compter des points entre deux instants | `histc(S, T)` ou une boucle | `np.diff(np.searchsorted(S, T))` | `searchsorted` suppose `S` trié |
| Minimum cumulé (Lindley) | `cummin(S)` | `np.minimum.accumulate(S)` |  |
| Fréquence d'un événement | `mean(L == 0)` | `np.mean(L == 0)` | Un booléen vaut 0 ou 1 |
| Moyenne, variance | `mean(L)`, `var(L)` | `L.mean()`, `L.var(ddof=1)` | `var` Matlab divise par $n - 1$ : `ddof=1` |
| Histogramme normalisé | `histc(L, 0:40) / n` | `np.bincount(L, minlength=41)[:41] / n` |  |
| Échelle log en ordonnée | `semilogy(k, p)` | `ax.set_yscale("log")` | Les fréquences nulles disparaissent en log |
| Trajectoire en escalier | `stairs(T, L)` | `ax.step(T, L, where="post")` |  |
| Graine | `rng(2026)` (Octave : `rand('twister', 2026)`) | `np.random.default_rng(2026)` | Générateurs différents : tirages différents |

Script Matlab complet : [`matlab/s4_file_mm1.m`](matlab/s4_file_mm1.m) (+ `matlab/nb_points_poisson.m`),
exécuté sous GNU Octave 8.4 ; équivalent Python ligne à ligne : [`matlab/s4_file_mm1.py`](matlab/s4_file_mm1.py).
Comparaison des sorties : annexe B du PDF.

| sortie | Octave (Mersenne Twister) | Python (PCG64) | théorie |
|---|---|---|---|
| $\mathcal P(4)$ : moyenne ; variance | 4,0519 ; 4,0064 | 4,0241 ; 3,9699 | 4 ; 4 |
| clients en 5 min ; file max | 30 174 ; 46 | 30 075 ; 31 | 30 000 en moyenne |
| $E[L]$ | 4,9854 | 4,8069 | 5 |
| $\operatorname{Var}L$ | 30,8240 | 23,5177 | 30 |
| $P(L = 0)$ | 0,1688 | 0,1655 | 0,1667 |
| $P(L > 5)$ | 0,3318 | 0,3355 | 0,3349 |

**À savoir pour l'oral.** La moyenne de $\mathcal P(4)$ sous Octave, $4{,}052$, est à $+2{,}6$
erreurs-types ($0{,}02$ pour $10^4$ tirages) : écart rare mais pas un biais. Avec les graines 1 à
10, les écarts vont de $-1{,}5$ à $+1{,}9$ erreur-type. La variance de $L$ est l'indicateur le plus
instable (23,5 et 30,8) car elle dépend des quelques longues files.

Le code réutilisable est dans `src/stats_td/files_attente.py` (`nombre_points_poisson`,
`poisson_comptage`, `file_mm1`, `file_mm1_vectorisee`, `file_mm1_evenements`, `longueur_lindley`,
`indicateurs_theoriques`, `moyenne_par_lots`).
