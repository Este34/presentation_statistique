# Sujet 4 · Démonstrations

Notations : $X \sim \mathcal E(\lambda)$ signifie « $X$ suit la loi exponentielle de paramètre
$\lambda > 0$ » ; $F^c(x) = P(X \ge x)$ est la fonction de répartition complémentaire ;
$\mathbb 1_A$ vaut 1 sur $A$ et 0 ailleurs ; $\mathcal P(m)$ est la loi de Poisson de paramètre $m$.
Les valeurs numériques viennent de `s4_1_file_mm1.ipynb` (graine 2026).

Convention d'indices (voir la coquille de l'énoncé, B.2) : $T_0 = 0$, $T_n = I_1 + \dots + I_n$ est
l'instant du $n$-ième événement, et $I_n = T_n - T_{n-1}$ sépare le $(n-1)$-ième et le $n$-ième.

---

<a id="a1"></a>

## A.1 · Moyenne et écart-type de $\mathcal E(\lambda)$

**Densité.** Pour $x \ge 0$, $F(x) = P(X \le x) = 1 - e^{-\lambda x}$ (car $P(X = x) = 0$ : la
fonction $F^c$ est continue). On dérive : $f(x) = \lambda e^{-\lambda x}\,\mathbb 1_{x \ge 0}$.

**Moyenne** (intégration par parties, IPP, avec $u = x$, $v' = \lambda e^{-\lambda x}$) :
```math
E[X] = \int_0^{\infty} x\,\lambda e^{-\lambda x}\,dx
     = \big[-x e^{-\lambda x}\big]_0^{\infty} + \int_0^{\infty} e^{-\lambda x}\,dx = 0 + \frac{1}{\lambda}.
```
Le crochet est nul : $x e^{-\lambda x} \to 0$ en $+\infty$ (l'exponentielle l'emporte) et vaut 0 en 0.

**Moment d'ordre 2** (même IPP avec $u = x^2$) :
```math
E[X^2] = \big[-x^2 e^{-\lambda x}\big]_0^{\infty} + 2\int_0^{\infty} x e^{-\lambda x}\,dx
       = \frac{2}{\lambda}\,E[X] = \frac{2}{\lambda^2}.
```
**Variance** (formule de König-Huygens) : $\operatorname{Var}X = E[X^2] - E[X]^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \frac{1}{\lambda^2}$.

```math
\boxed{E[X] = \sigma_X = \frac{1}{\lambda}}
```
La moyenne et l'écart-type sont égaux (coefficient de variation $\sigma/E = 1$).

**Remarques utiles à l'oral.**
- Unités : si $\lambda$ est en « événements par seconde », $1/\lambda$ est en secondes : c'est bien une durée.
- Formule plus rapide pour une variable positive : $E[X] = \int_0^\infty P(X \ge x)\,dx = \int_0^\infty e^{-\lambda x}dx = 1/\lambda$.
- Contrôle numérique : sur $10^5$ tirages de $\mathcal E(2)$, moyenne et écart-type empiriques valent tous deux $\approx 0{,}5$ (notebook, partie A).

---

<a id="a2"></a>

## A.2 · Absence de mémoire

Soient $x, t \ge 0$. Comme $t \ge 0$, l'événement $\{X \ge x + t\}$ est **inclus** dans $\{X \ge x\}$,
donc leur intersection est $\{X \ge x + t\}$. Et $P(X \ge x) = e^{-\lambda x} > 0$, donc on peut
conditionner :
```math
P(X \ge x + t \mid X \ge x) = \frac{P(X \ge x + t,\ X \ge x)}{P(X \ge x)} = \frac{P(X \ge x+t)}{P(X \ge x)}
= \frac{e^{-\lambda(x+t)}}{e^{-\lambda x}} = e^{-\lambda t} = P(X \ge t).
```
```math
\boxed{P(X \ge x + t \mid X \ge x) = P(X \ge t)\quad\text{pour tous } x, t \ge 0.}
```
**Sens.** Sachant que l'ampoule a déjà duré $x$, sa durée de vie **restante** $X - x$ a encore la
loi $\mathcal E(\lambda)$ : elle « ne vieillit pas ». Pour la file : quel que soit le temps
depuis lequel un client est servi, la durée de service qui lui reste suit $\mathcal E(\mu)$. C'est
la propriété qui rend la file M/M/1 simple à étudier.

---

<a id="a3"></a>

## A.3 · L'exponentielle est la seule loi sans mémoire

Hypothèses : $X \ge 0$ est une variable à densité (donc $P(X = x) = 0$ pour tout $x$) et
$G(x) = P(X \ge x) > 0$ pour tout $x \ge 0$ (sinon le conditionnement de $(*)$ n'a pas de sens).

**Étape 1 : équation fonctionnelle.** Comme à la question A.2, $(*)$ s'écrit
$\frac{G(x+t)}{G(x)} = G(t)$, soit
```math
G(x + t) = G(x)\,G(t) \qquad \text{pour tous } x, t \ge 0.
```
**Étape 2 : passage au logarithme.** $\varphi = \ln G$ est bien défini ($G > 0$) et vérifie
$\varphi(x + t) = \varphi(x) + \varphi(t)$ (équation de Cauchy). De plus $\varphi$ est
**décroissante**, car $G$ l'est (si $x \le y$, $\{X \ge y\} \subset \{X \ge x\}$).

**Étape 3 : sur les rationnels.** Par récurrence, $\varphi(n x) = n\,\varphi(x)$ pour $n \in \mathbb N$.
Avec $x = 1/q$ : $\varphi(1) = q\,\varphi(1/q)$, donc $\varphi(p/q) = p\,\varphi(1/q) = \frac{p}{q}\varphi(1)$.
Ainsi $\varphi(r) = r\,\varphi(1)$ pour tout rationnel $r \ge 0$.

**Étape 4 : sur les réels (par monotonie).** Soit $x \ge 0$ et des rationnels $r \le x \le r'$.
Par décroissance, $\varphi(r') \le \varphi(x) \le \varphi(r)$, soit $r'\varphi(1) \le \varphi(x) \le r\varphi(1)$.
En faisant tendre $r$ et $r'$ vers $x$ (les rationnels sont denses), $\varphi(x) = x\,\varphi(1)$.

**Étape 5 : conclusion.** On pose $\lambda = -\varphi(1) = -\ln G(1) \ge 0$. Si $\lambda = 0$, alors
$G \equiv 1$ : $P(X \ge x) = 1$ pour tout $x$, impossible pour une variable réelle
($P(X \ge x) \to 0$ quand $x \to +\infty$). Donc $\lambda > 0$ et
```math
\boxed{P(X \ge x) = e^{-\lambda x}\ (x \ge 0) : \quad X \sim \mathcal E(\lambda).}
```
**Version rapide (si $G$ est dérivable).** On dérive $G(x + t) = G(x)G(t)$ par rapport à $t$ en
$t = 0$ : $G'(x) = G'(0)\,G(x)$, équation différentielle de solution $G(x) = e^{G'(0)x}$
(car $G(0) = 1$). On retrouve $\lambda = -G'(0) = f(0)$.

**Remarques utiles à l'oral.**
- L'hypothèse « à densité » compte : en **discret**, la loi géométrique est elle aussi sans mémoire
  ($P(X \ge n + m \mid X \ge n) = P(X \ge m)$). L'exponentielle est son analogue continu.
- La monotonie remplace la continuité : sans aucune régularité, l'équation de Cauchy a des
  solutions « pathologiques », mais une fonction monotone n'en fait pas partie.

---

<a id="b1"></a>

## B.1 · Densité d'une somme : le produit de convolution

$X_1$ et $X_2$ sont **indépendantes**, donc le couple $(X_1, X_2)$ a pour densité le produit
$f(x_1)\,g(x_2)$. Pour $z \in \mathbb R$ :
```math
P(Z \le z) = \iint_{x_1 + x_2 \le z} f(x_1)\,g(x_2)\,dx_1\,dx_2
           = \int_{\mathbb R} f(x_1)\left(\int_{-\infty}^{z - x_1} g(x_2)\,dx_2\right) dx_1 .
```
Dans l'intégrale intérieure on pose $x_2 = s - x_1$ ($x_1$ fixé, $dx_2 = ds$, jacobien 1 ; la borne
$x_2 = z - x_1$ devient $s = z$) :
```math
P(Z \le z) = \int_{\mathbb R} f(x_1)\int_{-\infty}^{z} g(s - x_1)\,ds\,dx_1
           = \int_{-\infty}^{z}\underbrace{\left(\int_{\mathbb R} f(x_1)\,g(s - x_1)\,dx_1\right)}_{(f*g)(s)} ds .
```
L'échange des intégrales est permis par le **théorème de Fubini-Tonelli** (fonction positive). La
fonction de répartition de $Z$ est donc l'intégrale de $f * g$ :
```math
\boxed{f_Z(z) = (f*g)(z) = \int_{\mathbb R} f(x)\,g(z - x)\,dx.}
```

---

<a id="b2"></a>

## B.2 · Les instants $T_k$ suivent des lois d'Erlang

**$T_2$.** $T_2 = I_1 + I_2$ avec $I_1, I_2$ indépendantes de loi $\mathcal E(\lambda)$. Par B.1,
pour $x \ge 0$ :
```math
f_2(x) = \int_{\mathbb R} \lambda e^{-\lambda u}\mathbb 1_{u \ge 0}\ \lambda e^{-\lambda(x - u)}\mathbb 1_{x - u \ge 0}\,du
       = \lambda^2 e^{-\lambda x}\int_0^x du = \lambda^2 x\,e^{-\lambda x},
```
car les indicatrices limitent $u$ à $[0, x]$ et $e^{-\lambda u}e^{-\lambda(x-u)} = e^{-\lambda x}$ ne
dépend plus de $u$. Pour $x < 0$, $f_2(x) = 0$.

**Récurrence.** Hypothèse $\mathcal H_k$ : $T_k$ a pour densité
$f_k(x) = \frac{\lambda^k x^{k-1}}{(k-1)!}e^{-\lambda x}\mathbb 1_{x \ge 0}$.
- *Initialisation* : $f_1(x) = \lambda e^{-\lambda x}$, c'est la densité de $T_1 = I_1 \sim \mathcal E(\lambda)$.
- *Hérédité* : $T_{k+1} = T_k + I_{k+1}$, et $I_{k+1}$ est **indépendante** de $T_k$ (qui ne dépend
  que de $I_1, \dots, I_k$). Par B.1, pour $x \ge 0$ :
```math
f_{k+1}(x) = \int_0^x \frac{\lambda^k u^{k-1}}{(k-1)!}e^{-\lambda u}\ \lambda e^{-\lambda(x-u)}\,du
           = \lambda^{k+1}e^{-\lambda x}\int_0^x \frac{u^{k-1}}{(k-1)!}\,du
           = \frac{\lambda^{k+1}x^{k}}{k!}e^{-\lambda x}.
```
C'est $\mathcal H_{k+1}$. Donc pour tout $k \ge 1$ :
```math
\boxed{f_k(x) = \frac{\lambda^k x^{k-1}}{(k-1)!}\,e^{-\lambda x},\quad x \ge 0.}
```
**Contrôle** : $E[T_k] = k/\lambda$ et $\operatorname{Var}T_k = k/\lambda^2$ (somme de $k$ variables
indépendantes de moyenne $1/\lambda$ et de variance $1/\lambda^2$, A.1).

---

<a id="b3"></a>

## B.3 · Le nombre d'événements dans $[0, t]$ suit $\mathcal P(\lambda t)$

**L'indication.** Il y a exactement $k$ événements dans $[0, t]$ si et seulement si le $k$-ième a
eu lieu au plus tard en $t$ et le $(k+1)$-ième après $t$ : $\{N_t = k\} = \{T_k \le t < T_{k+1}\}$
(avec $T_0 = 0$).

**Différence de deux répartitions.** Comme $T_{k+1} \ge T_k$, on a
$\{T_{k+1} \le t\} \subset \{T_k \le t\}$, donc, en notant $F_k$ la fonction de répartition de $T_k$ :
```math
P(N_t = k) = P(T_k \le t) - P(T_{k+1} \le t) = F_k(t) - F_{k+1}(t).
```
**IPP** sur $F_{k+1}(t) = \int_0^t \frac{\lambda^{k+1}u^{k}}{k!}e^{-\lambda u}du$, avec $U = \frac{(\lambda u)^k}{k!}$
et $V' = \lambda e^{-\lambda u}$ (donc $V = -e^{-\lambda u}$), pour $k \ge 1$ :
```math
F_{k+1}(t) = \Big[-\frac{(\lambda u)^k}{k!}e^{-\lambda u}\Big]_0^t + \int_0^t \frac{\lambda^k u^{k-1}}{(k-1)!}e^{-\lambda u}\,du
           = -e^{-\lambda t}\frac{(\lambda t)^k}{k!} + F_k(t).
```
D'où, pour $k \ge 1$, et directement pour $k = 0$ ($P(N_t = 0) = P(T_1 > t) = e^{-\lambda t}$) :
```math
\boxed{P(N_t = k) = e^{-\lambda t}\frac{(\lambda t)^k}{k!} :\quad N_t \sim \mathcal P(\lambda t).}
```
**Remarques utiles à l'oral.**
- $E[N_t] = \lambda t$ : on retrouve « $\lambda$ = nombre moyen d'événements par unité de temps ».
- $N_t$ est fini presque sûrement : $T_k/k \to 1/\lambda$ (loi des grands nombres), donc $T_k \to \infty$.
- Par absence de mémoire, le nombre d'événements dans **tout** intervalle de longueur $s$ suit
  $\mathcal P(\lambda s)$, indépendamment de ce qui s'est passé avant : c'est ce qui sert pour $A_n$.

---

<a id="s1"></a>

## Simulation, Q1 · $X = -\frac{1}{\lambda}\ln U$ suit $\mathcal E(\lambda)$

$U \in\, ]0, 1]$ donc $\ln U \le 0$ et $X \ge 0$ : pour $x < 0$, $P(X \ge x) = 1$. Pour $x \ge 0$,
comme $\lambda > 0$ et que $\exp$ est **croissante** :
```math
P(X \ge x) = P\!\left(-\tfrac{1}{\lambda}\ln U \ge x\right) = P(\ln U \le -\lambda x) = P(U \le e^{-\lambda x}) = e^{-\lambda x},
```
car $P(U \le u) = u$ pour $u \in [0, 1]$ (ici $u = e^{-\lambda x} \in\, ]0, 1]$). On retrouve
exactement $F^c$ :
```math
\boxed{U \sim \mathcal U[0,1] \ \Rightarrow\ -\tfrac{1}{\lambda}\ln U \sim \mathcal E(\lambda).}
```
C'est la **méthode d'inversion** du sujet 1 : $F^{-1}(v) = -\frac{1}{\lambda}\ln(1-v)$, et $1 - U$ a
même loi que $U$. Dans le code on utilise $1 - U \in\, ]0,1]$ pour ne jamais calculer $\ln 0$.

---

<a id="s2"></a>

## Simulation, Q2 · Un algorithme pour $\mathcal P(\lambda)$

**Pourquoi la formule.** Les $Z_i = X_1 + \dots + X_i$ sont exactement les instants $T_i$ d'un
processus de Poisson d'intensité $\lambda$ (intervalles indépendants de loi $\mathcal E(\lambda)$).
$\sum_{i \ge 1}\mathbb 1_{Z_i \le 1}$ compte les événements tombés dans $[0, 1]$ : c'est $N_1$, de
loi $\mathcal P(\lambda \cdot 1)$ par B.3. (La somme est finie : $Z_i \to \infty$.)

**Algorithme** (on ajoute des durées exponentielles jusqu'à dépasser 1) :
```text
N ← 0 ; Z ← -ln(U)/λ          (U uniforme, Simulation Q1)
tant que Z ≤ 1 :
    N ← N + 1
    Z ← Z - ln(U')/λ          (U' nouvelle uniforme, indépendante)
renvoyer N
```
**Variante multiplicative (Knuth).** $Z_i \le 1 \iff \sum_{j \le i} -\ln U_j \le \lambda \iff
U_1 \cdots U_i \ge e^{-\lambda}$ : on multiplie des uniformes tant que le produit reste
$\ge e^{-\lambda}$, sans calculer de logarithme.

**Coût.** On tire $N + 1$ uniformes, donc $\lambda + 1$ en moyenne : parfait pour $\lambda$ petit
(c'est notre cas, $A_n$ a une moyenne $\approx 1{,}2$), lent si $\lambda$ est grand (on utilise
alors d'autres méthodes, par exemple celle de `numpy.random.Generator.poisson`).

**Pour un paramètre $m = \mu s$ quelconque** : on compte les sommes de durées $\mathcal E(\mu)$ qui
restent $\le s$, c'est-à-dire le nombre de points d'un processus de Poisson d'intensité $\mu$ dans
un intervalle de longueur $s$ (B.3, $\mathcal P(\mu s)$). C'est ce qu'on fait pour $A_n$.

---

<a id="m1"></a>

## M/M/1, Q1 · La récurrence $L_{n+1} = (L_n + 1 - A_n)^+$

**Le processus des « services potentiels ».** Tant que le serveur travaille, la durée de service
restante du client en cours suit $\mathcal E(\mu)$ quel que soit le temps déjà passé (A.2). Les
fins de service se produisent donc au rythme d'un processus de Poisson d'intensité $\mu$ tant que
la file n'est pas vide. On peut ainsi construire la file avec **un seul** processus de Poisson
$N(t)$ d'intensité $\mu$, indépendant des arrivées : chaque point de $N$ est un départ si au moins
un client est présent, et il est « perdu » si la file est vide. Le processus $L(t)$ obtenu a la
même loi que celui de la file M/M/1 (mêmes taux de saut : $+1$ au taux $\lambda$, $-1$ au taux
$\mu$ si $L \ge 1$).

**Entre deux arrivées.** Juste après l'arrivée du $n$-ième client (instant $T_n$), il y a
$L_n + 1$ clients. Sur $[T_n, T_{n+1}[$ il n'arrive personne, et $N$ y place
$A_n = N(T_{n+1}) - N(T_n)$ points. Chacun fait partir un client **tant qu'il en reste**. Le
nombre de départs est donc $D_n = \min(A_n, L_n + 1)$ (on ne peut pas faire partir plus de clients
qu'il n'y en a). D'où
```math
L_{n+1} = L_n + 1 - \min(A_n, L_n + 1) = \max(L_n + 1 - A_n,\ 0).
```
```math
\boxed{L_1 = 0,\qquad L_{n+1} = (L_n + 1 - A_n)^+.}
```
(Le crochet $[T_n, T_{n+1}[$ ou $]T_n, T_{n+1}]$ ne change rien : presque sûrement aucun point de $N$
ne tombe exactement sur un instant d'arrivée.)

**Loi de $A_n$.** Sachant $T_{n+1} - T_n = s$, $A_n \sim \mathcal P(\mu s)$ (B.3 appliqué à $N$ sur
un intervalle de longueur $s$). Comme $T_{n+1} - T_n \sim \mathcal E(\lambda)$ :
```math
P(A_n = k) = \int_0^\infty \lambda e^{-\lambda s}\, e^{-\mu s}\frac{(\mu s)^k}{k!}\,ds
           = \frac{\lambda\mu^k}{k!}\cdot\frac{k!}{(\lambda + \mu)^{k+1}}
           = \underbrace{\frac{\lambda}{\lambda+\mu}}_{p}\Big(\underbrace{\frac{\mu}{\lambda+\mu}}_{q}\Big)^k ,
```
(avec $\int_0^\infty s^k e^{-as}ds = k!/a^{k+1}$, $a = \lambda + \mu$). C'est une loi **géométrique**
sur $\{0, 1, 2, \dots\}$ : on compte les services avant la prochaine arrivée, comme dans une course
entre deux horloges exponentielles où le service gagne avec probabilité $q$. Moyenne
$E[A_n] = q/p = \mu/\lambda = 1/\rho$. Les $A_n$ portent sur des intervalles **disjoints** : ils sont
indépendants entre eux et indépendants de $L_n$ (qui ne dépend que de $A_1, \dots, A_{n-1}$).
$(L_n)$ est donc une **chaîne de Markov** : une marche aléatoire réfléchie en 0.

---

<a id="m2"></a>

## M/M/1, Q2 · Algorithme de simulation

```text
L[1] ← 0 ; t ← -ln(U)/λ                       (instant T_1 de la première arrivée)
pour n = 1, 2, ... tant que t ≤ durée :
    s ← -ln(U)/λ                               (écart T_{n+1} - T_n, loi E(λ), Simulation Q1)
    A ← nombre de sommes de durées E(μ) ≤ s    (A_n ~ P(μ s), Simulation Q2)
    L[n+1] ← max(0, L[n] + 1 - A)              (récurrence, Q1)
    t ← t + s
```
Variante équivalente, plus rapide (vectorisée) : tirer d'un coup tous les instants d'arrivée
$T_n$ (sommes cumulées de $\mathcal E(\lambda)$) et tous les points de $N$ sur $[0, \text{durée}]$
(sommes cumulées de $\mathcal E(\mu)$), puis compter les points de $N$ entre deux arrivées
(`np.searchsorted`). La récurrence elle-même se vectorise par la **formule de Lindley**
ci-dessous.

**Validation indépendante** (notebook) : une simulation « à événements » directe de la file
(chaque client a son propre temps de service $\mathcal E(\mu)$, FIFO) donne la même loi de $L_n$.

---

<a id="m3"></a>

## M/M/1, Q3 · Si $\rho > 1$, la file croît indéfiniment

**Formule de Lindley.** Posons $\Delta_k = 1 - A_k$ et $S_n = \sum_{k=1}^{n-1}\Delta_k$ ($S_1 = 0$).
Alors
```math
L_n = S_n - \min_{1 \le k \le n} S_k .
```
*Preuve par récurrence* : vrai pour $n = 1$ ($0 = 0 - 0$). Si c'est vrai au rang $n$, avec
$m_n = \min_{k \le n} S_k$ : $L_{n+1} = \max(0, S_n - m_n + \Delta_n) = \max(0, S_{n+1} - m_n)
= S_{n+1} - \min(S_{n+1}, m_n) = S_{n+1} - m_{n+1}$.

**Croissance linéaire.** En particulier $L_n \ge S_n$ (car $m_n \le S_1 = 0$). Les $\Delta_k$ sont
indépendants, de même loi, de moyenne $E[\Delta] = 1 - \frac{1}{\rho}$. Par la **loi forte des
grands nombres**, $S_n / n \to 1 - \frac1\rho > 0$ presque sûrement si $\rho > 1$. Donc
$S_n \to +\infty$, le minimum $m_n$ finit par ne plus bouger, et
```math
\boxed{\rho > 1 :\quad \frac{L_n}{n} \xrightarrow[n\to\infty]{\text{p.s.}} 1 - \frac{1}{\rho} > 0,
\qquad L(t) \approx (\lambda - \mu)\,t .}
```
(Il arrive $\approx \lambda t$ clients en un temps $t$, d'où $(1 - \mu/\lambda)\lambda t = (\lambda - \mu)t$.)
Avec $\lambda = 120$, $\mu = 100$ : $\rho = 1{,}2$, pente $1/6$ par client, soit $\approx 20$ clients
de plus par seconde. Simulation : voir le notebook (Q3).

**Cas limite $\rho = 1$** : $E[\Delta] = 0$, la marche est récurrente **nulle** : la file revient à
0 mais de plus en plus rarement, et $L_n$ est de l'ordre de $\sqrt n$. Pas de régime stationnaire
non plus.

---

<a id="m4"></a>

## M/M/1, Q4 · Si $\rho < 1$, la file se stationnarise

Si $\rho < 1$, $E[\Delta] = 1 - 1/\rho < 0$ : $S_n \to -\infty$ et la file revient sans cesse à 0
(chaîne **récurrente positive**). Une chaîne de Markov irréductible (on passe de tout état à tout
état), apériodique ($P(0 \to 0) > 0$) et récurrente positive a une **unique** loi stationnaire
$\pi$, et :
- $L_n$ converge **en loi** vers $\pi$ quel que soit le départ (ici la file vide) ;
- **théorème ergodique** : $\frac{1}{n}\sum_{k=1}^n L_k \to E_\pi[L]$ presque sûrement.

C'est ce que montre la simulation : la trajectoire fluctue autour d'un niveau fixe et la moyenne
cumulée se stabilise sur $\rho/(1-\rho)$ (Q5).

---

<a id="m5"></a>

## M/M/1, Q5 · La loi stationnaire est géométrique : $\pi_k = (1-\rho)\rho^k$

**Vérification de l'invariance.** Supposons $L_n \sim \pi$ et montrons $L_{n+1} \sim \pi$. Pour
$j \ge 1$, $L_{n+1} = j$ exige $A_n = L_n + 1 - j \ge 0$. En posant $m = A_n$ et en utilisant
l'indépendance de $L_n$ et $A_n$ :
```math
P(L_{n+1} = j) = \sum_{m \ge 0}\pi_{j-1+m}\,p\,q^m = (1-\rho)\rho^{j-1}\,p\sum_{m\ge0}(\rho q)^m
               = (1-\rho)\rho^{j-1}\,\frac{p}{1 - \rho q}.
```
Or $\rho q = \frac{\lambda}{\mu}\cdot\frac{\mu}{\lambda+\mu} = p$, donc $1 - \rho q = 1 - p = q$ et
$\frac{p}{1-\rho q} = \frac{p}{q} = \frac{\lambda}{\mu} = \rho$ :
$P(L_{n+1} = j) = (1-\rho)\rho^{j}$. Pour $j = 0$ le résultat suit car les probabilités somment à
1. (La série converge car $\rho q < 1$.) Donc $\pi$ est invariante, et par Q4 c'est **la** loi
limite :
```math
\boxed{P(L_n = k) \xrightarrow[n\to\infty]{} (1-\rho)\rho^k,\qquad \rho = \frac{\lambda}{\mu} < 1.}
```
C'est une loi géométrique sur $\{0, 1, 2, \dots\}$ (nombre d'échecs avant le premier succès, succès
de probabilité $1 - \rho$).

**Expressions analytiques.** On utilise $\sum_{k\ge0}\rho^k = \frac{1}{1-\rho}$ et ses dérivées
$\sum_k k\rho^{k-1} = \frac{1}{(1-\rho)^2}$, $\sum_k k(k-1)\rho^{k-2} = \frac{2}{(1-\rho)^3}$ (on
dérive une série entière terme à terme dans son disque de convergence).
- Moyenne : $E[L] = (1-\rho)\rho\sum_k k\rho^{k-1} = \dfrac{\rho}{1-\rho}$.
- Variance : $E[L(L-1)] = (1-\rho)\rho^2\frac{2}{(1-\rho)^3} = \frac{2\rho^2}{(1-\rho)^2}$, puis
  $\operatorname{Var}L = E[L(L-1)] + E[L] - E[L]^2 = \frac{2\rho^2 + \rho(1-\rho) - \rho^2}{(1-\rho)^2} = \dfrac{\rho}{(1-\rho)^2}$.
- Serveur libre à l'arrivée : $P(L = 0) = 1 - \rho$.
- Plus de 5 clients devant soi : $P(L > 5) = \sum_{k \ge 6}(1-\rho)\rho^k = (1-\rho)\frac{\rho^6}{1-\rho} = \rho^6$
  (et plus généralement $P(L \ge k) = \rho^k$).

| quantité | formule | $\rho = 5/6$ ($\lambda = 100$, $\mu = 120$) |
|---|---|---|
| $E[L]$ | $\rho/(1-\rho)$ | $5$ |
| $\operatorname{Var} L$ | $\rho/(1-\rho)^2$ | $30$ (écart-type $5{,}48$) |
| $P(\text{serveur libre})$ | $1-\rho$ | $1/6 \approx 0{,}1667$ |
| $P(L > 5)$ | $\rho^6$ | $(5/6)^6 \approx 0{,}3349$ |

**Remarques utiles à l'oral.**
- **Pourquoi « juste avant une arrivée » donne la même loi que « à un instant quelconque »** :
  propriété PASTA (*Poisson Arrivals See Time Averages*) : des arrivées poissoniennes voient la
  file dans son état moyen. (Pour des arrivées régulières, ce serait faux.)
- **Temps moyen passé dans le système** par un client : il attend la fin des $L$ services devant
  lui puis le sien, chacun de moyenne $1/\mu$ (absence de mémoire pour le client en cours), d'où
  $E[W] = \frac{E[L] + 1}{\mu} = \frac{1}{\mu - \lambda} = 50$ ms. On retrouve la **formule de
  Little** $E[L] = \lambda\,E[W]$ : $100 \times 0{,}05 = 5$.
- **$\rho$ proche de 1** : $E[L] = \rho/(1-\rho)$ explose. Passer de $\rho = 0{,}8$ à $0{,}9$
  double la file moyenne (4 puis 9) ; à $0{,}99$ elle vaut 99. C'est le message « capital » du TD.
- **Incertitude de la simulation** : les $L_n$ successifs sont **corrélés** (la file change d'au
  plus 1 vers le haut entre deux arrivées). L'erreur-type naïve $\hat\sigma/\sqrt n$ est trop
  optimiste ; on utilise la **méthode des lots** (moyennes de blocs de 10 s, à peu près
  indépendantes). Voir le notebook, Q5.
