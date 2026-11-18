# Sujet 3 — Fiche de révision (recuit simulé)

## L'essentiel en 5 lignes
1. $h(x) = x^2 + 3x\cos x$ n'est **pas convexe** : 9 minima locaux sur $[-8\pi, 8\pi]$, global en $x^\star = -0{,}637$.
2. **Gradient** : on descend la pente, $x_{n+1} = x_n - \frac{0{,}025}{n}h'(x_n)$ → minimum **local** du bassin de $x_0$ (8,814), en $n^{-0{,}5}$.
3. **Recuit** : on accepte parfois de monter, avec probabilité $e^{-\Delta h/T_n}$ ; $T$ grand = exploration, $T$ petit = descente.
4. Fondement : loi stationnaire $\mu_T \propto e^{-h/T}$ (Boltzmann), qui se concentre sur les minima globaux quand $T \to 0$.
5. Avec $T_n = 500 \times 0{,}99^n$ : **pas de garantie**, la chaîne gèle (Borel-Cantelli) ; Hajek demande $c/\ln n$ ; 74 % de succès, 26 % piégés en 2,805.

## Formules
| objet | formule |
|---|---|
| dérivées | $h' = 2x + 3\cos x - 3x\sin x$ ; $h'' = 2 - 6\sin x - 3x\cos x$ |
| minoration | $h(x) \ge \lvert x\rvert(\lvert x\rvert - 3) > 0$ si $\lvert x\rvert > 3$ ⇒ global dans $]-3,3[$ |
| descente | $h(x - \alpha h') \approx h(x) - \alpha h'^2$ |
| pas | $\sum\alpha_n = \infty$ (aller assez loin), $\sum \alpha_n^2 < \infty$ (pas qui s'éteignent) |
| vitesse gradient | $e_{n+1} \approx (1 - c/n)e_n$ ⇒ $\lvert e_n\rvert \approx Cn^{-c}$, $c = 0{,}025\,h''(\bar x)$, $e_n = x_n - \bar x$ |
| acceptation | $p = \min(1, e^{-\Delta h/T})$ ; accepter si $U < p$ car $P(U < p) = p$ |
| équilibre détaillé | $\mu_T(x)\,g\,\min(1, e^{-(h(y)-h(x))/T}) = g\min(\mu_T(x), \mu_T(y))$ |
| Hajek (espace fini) | $T_n = c/\ln n$, convergence **en probabilité** ssi $c \ge d^\star$ (profondeur max) |
| erreur-type d'une proportion | $\sqrt{\hat p(1-\hat p)/R}$ ; IC 95 % : $\pm 1{,}96\times$ |

## Chiffres à connaître (graine 2026)
| quantité | valeur |
|---|---|
| minimum global | $x^\star = -0{,}6371$, $h = -1{,}1305$ |
| piège | $x = 2{,}8051$, $h = -0{,}0748$ ; col en $1{,}227$, $h = 2{,}746$ (profondeur 2,82) |
| minimum local de $x_0 = 7{,}5$ | $x = 8{,}8137$, $h = 56{,}03$ ; $h''= 20{,}2$ |
| gradient, $N = 1000$ | $x_N = 8{,}661$, $h = 56{,}25$, écart 0,153 |
| gradient, écarts $n = 10^3, 10^4, 10^5$ | 0,153 ; 0,051 ; 0,016 ; pente $-0{,}494$ (théorie $-0{,}505$) |
| recuit, 1 lancer | $x_N = -0{,}650$, $h = -1{,}1298$ ; $T_N = 0{,}022$ ; $T = 1$ à $n = 618$ |
| acceptation | 0,99 (100 premières it.) → 0,09 (100 dernières) |
| Q4, écart final au global $h(x_N) - h(x^\star)$ | gradient 57,38 ; recuit $6{,}2\times10^{-4}$ |
| Q4, recuit dans le bassin du global | dès $n = 250$, définitivement à $n = 617$ ; 266 montées acceptées |
| Q4, Octave (autres tirages) | recuit $x_N = -0{,}698$, écart $1{,}3\times10^{-2}$ ; gradient identique |
| *(réserve)* recuit, 1000 lancers | global 73,8 % ± 2,7 % ; piège 25,9 % ± 2,7 % ; ailleurs 0,3 % |
| refroidissement lent ($\alpha = 0{,}995$, $N = 2000$) | 77,0 % ± 4,1 % (écart 1,27 e.-t., non significatif) |
| profondeur max $d^\star$ | 26,2 à petits pas, $\approx 12{,}3$ avec sauts $\pm\pi/2$ (minimum en $-24{,}44$) |

## Pièges
- Le signe du gradient : **moins** $\alpha_n h'$.
- « Le gradient converge vers le minimum » : **local**, et lentement.
- Un seul lancer du recuit ne prouve rien : évaluer sur plusieurs lancers avec un IC.
- « Garantit la convergence presque sûre » (énoncé) : faux, la chaîne gèle (Borel-Cantelli).
- Hajek : convergence **en probabilité**, pas presque sûre.
- Notation : $x^\star$ = minimum global ($-0{,}637$), $\bar x$ = minimum local du bassin de 7,5 ($8{,}814$).
- $\alpha$ désigne deux choses dans l'énoncé (pas du gradient, facteur de refroidissement).
- La grille $(n-1)/5000$ n'atteint pas $8\pi$.
