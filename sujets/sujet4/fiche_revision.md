# Sujet 4 · Fiche de révision (file M/M/1)

## L'essentiel en 5 lignes

**Message du TD** : la charge $\rho = \lambda/\mu$ décide de tout. Si $\rho < 1$ la file se
stabilise (loi géométrique), si $\rho > 1$ elle croît sans fin, et près de 1 tout explose.

1. $\mathcal E(\lambda)$ : moyenne = écart-type = $1/\lambda$, et c'est la **seule** loi (à densité) **sans mémoire**.
2. Processus de Poisson : écarts $\mathcal E(\lambda)$ indépendants ⇒ $T_k$ suit Erlang($k$, $\lambda$) (convolution) ⇒ $N_t \sim \mathcal P(\lambda t)$.
3. Simuler : $-\ln(1-U)/\lambda \sim \mathcal E(\lambda)$ ; $\mathcal P(\lambda)$ = nombre de sommes d'exponentielles $\le 1$.
4. File : $L_{n+1} = (L_n + 1 - A_n)^+$, $A_n$ = services **possibles** entre deux arrivées (géométrique, moyenne $\mu/\lambda$).
5. $\rho < 1$ : $P(L = k) = (1-\rho)\rho^k$, $E[L] = \frac{\rho}{1-\rho}$ ; $\rho > 1$ : $L(t) \approx (\lambda - \mu)t$.

## Formules
| objet | formule |
|---|---|
| exponentielle | $f(x) = \lambda e^{-\lambda x}$, $P(X \ge x) = e^{-\lambda x}$, $E = \sigma = 1/\lambda$ |
| sans mémoire | $P(X \ge x + t \mid X \ge x) = P(X \ge t)$ ⟺ $G(x+t) = G(x)G(t)$ |
| convolution | $f_{X_1 + X_2}(z) = \int f(x)\,g(z - x)\,dx$ (si indépendantes) |
| Erlang | $f_k(x) = \frac{\lambda^k x^{k-1}}{(k-1)!}e^{-\lambda x}$, $E[T_k] = k/\lambda$ |
| Poisson | $P(N_t = k) = e^{-\lambda t}\frac{(\lambda t)^k}{k!}$, via $\{N_t = k\} = \{T_k \le t < T_{k+1}\}$ |
| loi de $A_n$ | $P(A_n = k) = p\,q^k$, $p = \frac{\lambda}{\lambda+\mu}$, $q = \frac{\mu}{\lambda+\mu}$, $E[A] = \mu/\lambda$ |
| Lindley | $L_n = S_n - \min_{k \le n}S_k$, $S_n = \sum_{k<n}(1 - A_k)$ |
| $\rho > 1$ | $L_n/n \to 1 - 1/\rho$ (LGN), $L(t) \approx (\lambda - \mu)t$ |
| stationnaire | $\pi_k = (1-\rho)\rho^k$ ; clé : $\rho q = p$ |
| indicateurs | $E[L] = \frac{\rho}{1-\rho}$, $\operatorname{Var}L = \frac{\rho}{(1-\rho)^2}$, $P(L=0) = 1-\rho$, $P(L \ge k) = \rho^k$ |
| temps de séjour | $E[W] = \frac{E[L]+1}{\mu} = \frac{1}{\mu - \lambda}$ ; Little : $E[L] = \lambda E[W]$ |
| erreur-type par lots | $B$ lots, moyennes $\bar x_b$ : $\text{e.-t.} = \operatorname{sd}(\bar x_b)/\sqrt B$ (ddof=1) |

## Chiffres à connaître (graine 2026)
| quantité | valeur |
|---|---|
| $\mathcal E(2)$, $10^5$ tirages | moyenne $0{,}498$ ($-1{,}5$ e.-t.), écart-type $0{,}499$, KS $p = 0{,}15$ |
| survie résiduelle à $t = 0{,}5$ | expo : $0{,}366$ ; $0{,}368$ ; $0{,}369$ (âges 0 ; 0,5 ; 1) ; Erlang(2) : $0{,}735$ ; $0{,}551$ ; $0{,}487$ |
| $T_1, T_2, T_5$ | moyennes $0{,}499$ ; $1{,}001$ ; $2{,}497$ ; KS $p = 0{,}99$ ; $0{,}99$ ; $0{,}64$ |
| $\mathcal P(4)$ par comptage | moyenne $3{,}99$, variance $3{,}96$, $\chi^2$ $p = 0{,}37$ |
| Q1, petite trajectoire | 12 arrivées, $L_n = 0,0,0,0,0,1,0,1,2,2,1,0$ ; $A_3 = 6$ (5 services perdus) |
| Q2, validation (5 min, $\rho = 5/6$) | $E[L]$ : 4,96 / 5,05 / 5,20 ; $P(L=0)$ : 0,155 / 0,165 / 0,161 ; tous à 2 e.-t. au plus |
| Q3, $\rho = 1{,}2$, 60 s | 1099 clients ; pente $18{,}4$/s (théorie 20) ; $L_n/n = 0{,}154$ (théorie $0{,}167$) |
| Q3, $\rho = 1{,}05$, 60 s | 316 clients ; $L_n/n = 0{,}050$ (théorie $0{,}048$) |
| Q4, $\rho = 0{,}6$ et $0{,}9$, 120 s | moyennes $1{,}44 \pm 0{,}08$ (1,5) et $10{,}1 \pm 1{,}8$ (9) ; max 14 et 64 |
| Q5, 5 min | 30 070 clients, max 35 |
| Q5, $E[L]$ | $5{,}03 \pm 0{,}36$ (théorie 5, $+0{,}08$ e.-t.) |
| Q5, $\operatorname{Var}L$ | $29{,}1$ (théorie 30) |
| Q5, $P(L = 0)$ | $0{,}162 \pm 0{,}010$ (théorie $0{,}167$, $-0{,}51$ e.-t.) |
| Q5, $P(L > 5)$ | $0{,}340 \pm 0{,}023$ (théorie $0{,}335$, $+0{,}22$ e.-t.) |
| erreur-type naïve / par lots | $0{,}031$ / $0{,}355$ (rapport 11) ; autocorrélation $0{,}97$ (1 client), $0{,}18$ (100), $-0{,}01$ (1000) |
| *(réserve)* temps de séjour | $43{,}9 \pm 2{,}1$ ms pour 50 ; 40 graines : $50{,}5$ ms, écart-type $3{,}0$ : pas de biais |
| *(réserve)* $E[L]$ selon $\rho$ | 0,8 : $4{,}55$ (4) ; 0,9 : $9{,}16$ (9) ; 0,95 : $15{,}6 \pm 2{,}3$ (19) |
| Octave (autres tirages) | $E[L] = 4{,}99$, Var $30{,}8$, $P(L=0) = 0{,}169$, $P(L>5) = 0{,}332$ |

## Pièges
- $\rho = \lambda/\mu$, **pas** $\mu/\lambda$ (coquille de la Q5).
- $L$ compte aussi le client **en service**.
- « Plus de 5 » : $P(L > 5) = \rho^6$, pas $\rho^5$.
- $N(t)$ compte les services **possibles**, pas les départs : d'où le $\max(0, \cdot)$.
- « Se stationnarise » : c'est la **loi** qui converge, la trajectoire continue de fluctuer.
- Erreur-type : les $L_n$ sont **corrélés**, $\hat\sigma/\sqrt n$ est 11 fois trop petit.
- $\ln 0$ : utiliser $1 - U$ ; $\log$ = logarithme népérien.
- $\{N_t = k\} = \{T_k \le t < T_{k+1}\}$ : différence de répartitions, pas un produit.
- Variance empirique avec `ddof=1` (comme `var` de Matlab).
