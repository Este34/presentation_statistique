# Sujet 1 — Démonstrations

Notations : $U \sim \mathcal U[0,1]$ a pour fonction de répartition $F_U(u) = u$ sur $[0,1]$
(0 avant, 1 après) ; $\mathbb 1_A$ est l'indicatrice de l'ensemble $A$.

---

<a id="s11-q1"></a>

## 1.1 Q1 — Méthode d'inversion

**Énoncé.** $G$ croissante bijective (d'un intervalle de $[0,1]$ vers $\mathbb R$). Alors
$Y = G(U)$ a pour fonction de répartition $F_Y$ $\iff$ $G = F_Y^{-1}$.

**Preuve.** $G$ est strictement croissante, donc $G^{-1}$ aussi, et elles conservent l'ordre :
```math
G(U) \le y \iff U \le G^{-1}(y).
```
Donc, pour $G^{-1}(y) \in [0,1]$,
```math
\boxed{P(G(U) \le y) = P\big(U \le G^{-1}(y)\big) = F_U\big(G^{-1}(y)\big) = G^{-1}(y).}
```

- ($\Leftarrow$) Si $G = F_Y^{-1}$, alors $G^{-1} = F_Y$ et $P(G(U)\le y) = F_Y(y)$ : $Y$ a la
  bonne loi.
- ($\Rightarrow$) Si $P(G(U) \le y) = F_Y(y)$ pour tout $y$, alors $G^{-1}(y) = F_Y(y)$ pour tout
  $y$, c'est-à-dire $G^{-1} = F_Y$, soit $G = F_Y^{-1}$.

**Remarques utiles à l'oral.**
- *Pourquoi croissante ?* Une fonction décroissante renverserait l'inégalité :
  $P(G(U) \le y) = P(U \ge G^{-1}(y)) = 1 - G^{-1}(y)$. On aurait alors $G(u) = F_Y^{-1}(1-u)$,
  ce qui marche aussi puisque $1-U \sim \mathcal U[0,1]$.
- *Si* $F_Y$ *n'est pas bijective* (loi discrète, paliers) : on utilise l'**inverse généralisée**
  $`F_Y^{-1}(u) = \inf\{y : F_Y(y) \ge u\}`$ et le résultat reste vrai.
- *Limite de la méthode* : il faut connaître $F_Y^{-1}$ explicitement, ce qui n'est pas le cas
  de la gaussienne. D'où Box-Muller.

---

<a id="s11-q2"></a>

## 1.1 Q2 — Inversion de la loi exponentielle

Densité $f_Y(y) = \lambda e^{-\lambda y}\mathbb 1_{\mathbb R^+}(y)$ et fonction de répartition
$F_Y(y) = (1 - e^{-\lambda y})\mathbb 1_{\mathbb R^+}(y)$, d'où
$F^c_Y(y) = 1 - F_Y(y) = e^{-\lambda y}\mathbb 1_{\mathbb R^+}(y) + \mathbb 1_{\mathbb R^{*-}}(y)$.

Pour $u \in [0,1[$ :
```math
u = 1 - e^{-\lambda y} \iff e^{-\lambda y} = 1 - u \iff \boxed{y = F_Y^{-1}(u) = -\frac{\ln(1-u)}{\lambda}}
```

Comme $1-U \sim \mathcal U[0,1]$, $Y = -\ln(U)/\lambda$ suit la même loi. En pratique,
`rand`/`rng.random` tirent dans $[0,1[$ : on garde $1-U \in ]0,1]$ pour ne jamais calculer
$\ln 0$.

---

<a id="s11-q3"></a>

## 1.1 Q3 — Moyenne et variance de $\mathcal E(\lambda)$

**Moyenne** (intégration par parties, $u = y$, $dv = \lambda e^{-\lambda y}dy$, $v = -e^{-\lambda y}$) :
```math
\mathbb E[Y] = \int_0^{+\infty} y\,\lambda e^{-\lambda y}dy
= \Big[-y e^{-\lambda y}\Big]_0^{+\infty} + \int_0^{+\infty} e^{-\lambda y}dy
= 0 + \frac1\lambda = \boxed{\frac1\lambda}
```

**Moment d'ordre 2** (même intégration par parties avec $u = y^2$) :
```math
\mathbb E[Y^2] = \Big[-y^2 e^{-\lambda y}\Big]_0^{+\infty} + \int_0^{+\infty} 2y\,e^{-\lambda y}dy
= \frac{2}{\lambda}\int_0^{+\infty} y\,\lambda e^{-\lambda y}dy = \frac2\lambda\cdot\frac1\lambda = \frac{2}{\lambda^2}
```

**Variance** (formule de König-Huygens) :
```math
\mathrm{Var}(Y) = \mathbb E[Y^2] - \mathbb E[Y]^2 = \frac{2}{\lambda^2} - \frac{1}{\lambda^2} = \boxed{\frac{1}{\lambda^2}}
```

Pour $\lambda = 2$ : $\mathbb E[Y] = 0{,}5$ et $\mathrm{Var}(Y) = 0{,}25$ (l'écart-type est
égal à la moyenne, une propriété caractéristique de l'exponentielle).

**Estimateurs empiriques.**
$\bar Y = \frac1T\sum Y_i$ et $S^2 = \frac{1}{T-1}\sum (Y_i - \bar Y)^2$ (sans biais : on divise
par $T-1$ car $\bar Y$ est lui-même estimé ; c'est ce que fait `cov`/`var` de Matlab, et
`np.var(ddof=1)` en Python).

**Précision.** $\mathrm{Var}(\bar Y) = \sigma^2/T$, donc l'erreur-type vaut
$\sigma/\sqrt T = 0{,}5/100 = 0{,}005$. Par le TCL, $\bar Y$ tombe dans
$1/\lambda \pm 1{,}96 \times 0{,}005$ avec une probabilité d'environ 95 %. Pour la variance empirique
d'une exponentielle, $\mathrm{Var}(S^2) \approx (\mu_4 - \sigma^4)/T$ avec
$\mu_4 = 9/\lambda^4$, soit un écart-type $\approx \sqrt{8/T}/\lambda^2 \approx 0{,}007$.

---

<a id="s11-q4"></a>

## 1.1 Q4 — Droite en semi-log

$F^c_Y(y) = e^{-\lambda y} \Rightarrow \ln F^c_Y(y) = -\lambda y$ : en échelle logarithmique sur
l'axe vertical (`semilogy`), on obtient une droite passant par $(0, 1)$, de pente $-\lambda$
(en $\ln$ ; avec un $\log_{10}$, la pente vaut $-\lambda/\ln 10$).

L'énoncé dit « pente voisine de $\lambda$ » : il s'agit de sa valeur absolue, la droite est
décroissante.

Estimateur empirique : $`F^c_T(y) = \frac1T \#\{i : Y_i \ge y\}`$. Dans la queue, il ne reste que
quelques points : $F^c_T$ devient une marche d'escalier (avec un minimum de $1/T = 10^{-4}$), d'où
la régression faite sur la partie bien peuplée.

---

<a id="s12-q1"></a>

## 1.2 Q1 — $Z = X_1^2 + X_2^2 \sim \mathcal E(1/2)$

$X_1, X_2$ indépendantes $\Rightarrow$ densité jointe = produit des densités :
```math
f(x_1, x_2) = \frac{1}{\sqrt{2\pi}}e^{-x_1^2/2}\cdot\frac{1}{\sqrt{2\pi}}e^{-x_2^2/2} = \frac{1}{2\pi}e^{-\frac{x_1^2+x_2^2}{2}}.
```

Pour $z \ge 0$ :
```math
P(Z \ge z) = \iint_{x_1^2+x_2^2 \ge z} \frac{1}{2\pi}e^{-\frac{x_1^2+x_2^2}{2}}dx_1\,dx_2.
```

Changement de variables polaire : $x_1 = r\cos\theta$, $x_2 = r\sin\theta$, avec $r \ge 0$ et
$\theta \in [0, 2\pi[$. Le **jacobien** vaut
```math
\left|\det\begin{pmatrix}\cos\theta & -r\sin\theta\\ \sin\theta & r\cos\theta\end{pmatrix}\right| = r(\cos^2\theta + \sin^2\theta) = r,
```
donc $`dx_1\,dx_2 = r\,dr\,d\theta`$, et le domaine $x_1^2 + x_2^2 \ge z$ devient $r \ge \sqrt z$ :
```math
P(Z \ge z) = \int_0^{2\pi}\frac{d\theta}{2\pi}\int_{\sqrt z}^{+\infty} r\,e^{-r^2/2}dr
= 1 \times \Big[-e^{-r^2/2}\Big]_{\sqrt z}^{+\infty} = \boxed{e^{-z/2}}.
```

Pour $z < 0$, $P(Z \ge z) = 1$ (car $Z \ge 0$). Donc
$P(Z \ge z) = e^{-z/2}\mathbb 1_{\mathbb R^+}(z) + \mathbb 1_{\mathbb R^{*-}}(z)$ : c'est
$\mathcal E(\lambda = 1/2)$, de moyenne 2. Cohérent avec $\mathbb E[Z] = \mathbb E[X_1^2] + \mathbb E[X_2^2] = 1 + 1 = 2$.
(L'énoncé écrit $\exp(-2z)$ : coquille.)

> Culture : $Z$ suit aussi un $\chi^2$ à 2 degrés de liberté, et $\chi^2_2 = \mathcal E(1/2)$.

---

<a id="s12-q2"></a>

## 1.2 Q2 — Lois de $r^2$ et de $\theta$

$r^2 = X_1^2 + X_2^2 = Z$, donc $r^2 \sim \mathcal E(1/2)$ par Q1.

Densité de $(r, \theta)$ par le changement de variables (jacobien $r$) :
```math
f_{r,\theta}(r,\theta) = f(r\cos\theta, r\sin\theta)\cdot r = \underbrace{r\,e^{-r^2/2}\mathbb 1_{r\ge0}}_{g(r)}\cdot\underbrace{\frac{1}{2\pi}\mathbb 1_{[0,2\pi[}(\theta)}_{h(\theta)}.
```
La densité jointe **se factorise** en une fonction de $r$ seule et une fonction de $\theta$
seule, donc $r$ et $\theta$ sont **indépendants**. De plus $h$ est la densité de
$\mathcal U[0, 2\pi]$.

*Intuition* : la densité gaussienne 2D ne dépend que de $x_1^2 + x_2^2$ (isotrope, invariante
par rotation), donc aucune direction n'est privilégiée et l'angle est uniforme.

---

<a id="s12-q3"></a>

## 1.2 Q3 — Algorithme de Box-Muller

On inverse la démarche : on génère $(r, \theta)$ avec la bonne loi, puis on revient en
cartésiennes.
1. $U_1, U_2 \sim \mathcal U[0,1]$ indépendantes.
2. $r^2 = -2\ln U_1$ : inversion de $\mathcal E(1/2)$ ($-\ln(U)/\lambda$ avec $\lambda = 1/2$).
3. $\theta = 2\pi U_2 \sim \mathcal U[0, 2\pi]$, indépendante de $r$ car $U_1 \perp U_2$.
4. $X_1 = \sqrt{-2\ln U_1}\cos(2\pi U_2)$ et $X_2 = \sqrt{-2\ln U_1}\sin(2\pi U_2)$.

Le couple $(r, \theta)$ ainsi construit a exactement la loi de Q2 ; comme le changement de
variables polaire est une bijection, $(X_1, X_2)$ a la loi du couple de départ : deux
$\mathcal N(0,1)$ **indépendantes**.

> Variante (culture) : la **méthode polaire de Marsaglia** évite $\cos$ et $\sin$ en tirant
> un point uniforme dans le disque unité (par rejet).

---

<a id="s12-q4"></a>

## 1.2 Q4 — De $\mathcal N(0,1)$ à $\mathcal N(\mu, \sigma^2)$

```math
\boxed{Y = \mu + \sigma X}, \quad X \sim \mathcal N(0,1)
```

$`\mathbb E[Y] = \mu + \sigma\,\mathbb E[X] = \mu`$ et $\mathrm{Var}(Y) = \sigma^2\mathrm{Var}(X) = \sigma^2$.
Par changement de variable, $`f_Y(y) = \frac1\sigma f_X\!\left(\frac{y-\mu}{\sigma}\right) = \frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{(y-\mu)^2}{2\sigma^2}}`$ :
une transformation affine d'une gaussienne reste gaussienne.

Pour $\mathcal N(\mu = 5, \sigma^2 = 4)$ : $Y = 5 + 2X$. ⚠️ On multiplie par $\sigma = 2$, pas par
$\sigma^2 = 4$.

---

<a id="s12-q5"></a>

## 1.2 Q5 — Vérification

Les attendus sont $\bar Y \approx 5$ (erreur-type $\sigma/\sqrt T = 0{,}02$) et $S^2 \approx 4$
(écart-type de $S^2$ $\approx \sigma^2\sqrt{2/(T-1)} \approx 0{,}057$ pour une gaussienne).
L'histogramme normalisé (aire 1, `density=True`) doit épouser la densité
$\frac{1}{2\sqrt{2\pi}}e^{-(y-5)^2/8}$.
