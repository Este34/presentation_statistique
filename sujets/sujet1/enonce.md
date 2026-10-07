# Sujet 1 — Génération de variables aléatoires : 1ère partie

> Transcription de l'énoncé papier (pages 14-15). Les fonctions Matlab citées sont traduites
> en Python dans [matlab_python.md](matlab_python.md).

Dans ce STP nous abordons le problème de la génération de variables aléatoires distribuées
suivant une certaine loi.

## 1.1 Par inversion de la fonction de répartition

La méthode la plus simple pour générer une variable aléatoire $Y$ distribuée suivant une loi
de fonction de répartition $F_Y(y) = P(Y \le y)$ consiste à se procurer un bon générateur de
variable uniformément distribuée sur $[0,1]$, à générer $U \sim \mathcal U[0,1]$ et à utiliser
la transformation $Y = F_Y^{-1}(U)$.

1. Soit $U \sim \mathcal U[0,1]$ et soit $G$ une fonction croissante bijective. Donner
   l'expression de $P(G(U) \le y)$ et en déduire que $Y = G(U)$ a pour fonction de répartition
   $F_Y(\bullet)$ si et seulement si $G = F_Y^{-1}$.
2. Générer à l'aide de cette méthode une variable aléatoire $Y$ distribuée suivant la loi
   exponentielle de moyenne $1/\lambda$ notée $\mathcal E(\lambda)$ (prendre par exemple
   $\lambda = 2$). La loi exponentielle de moyenne $1/\lambda$ a pour fonction de répartition
   complémentaire
   $F^c_Y(y) = P(Y \ge y) = 1 - F(y) \exp(-\lambda y)\mathbb 1_{\mathbb R^+}(y) + \mathbb 1_{\mathbb R^{*-}}(y)$.
   > ⚠️ **Coquille** : la bonne formule est
   > $`F^c_Y(y) = \exp(-\lambda y)\,\mathbb 1_{\mathbb R^+}(y) + \mathbb 1_{\mathbb R^{*-}}(y)`$.
3. Générer $T = 10000$ variables aléatoires indépendantes de loi $\mathcal E(\lambda)$ (on prend
   toujours $\lambda = 2$). Démontrer l'expression analytique de la moyenne et de la variance de
   $\mathcal E(\lambda)$ en fonction de $\lambda$. Calculer la moyenne et la variance empirique
   de l'échantillon généré et commenter.
4. Vérifier la décroissance exponentielle $F^c_Y(y) = \exp(-\lambda y)$ ($y \ge 0$) de la
   fonction de répartition complémentaire de l'échantillon ainsi généré (représentation de la
   fonction de répartition complémentaire en échelle semilogarithmique) ; vérifier que la pente
   de la droite obtenue est voisine de $\lambda$.

**Fonctions Matlab à utiliser** : `rand` ; `mean`, `cov`, `std` ; `hist` + `cumsum` (estimateur
de la fonction de répartition) ; `semilogx`, `semilogy` ; `ginput` (coordonnées d'un point).

## 1.2 Génération de variables aléatoires gaussiennes par la méthode de Box et Muller

Une loi qui apparaît très fréquemment dans la nature (sa fréquence d'apparition est liée au
Théorème Central Limite) est la loi gaussienne. On dispose souvent (fonction `randn` en Matlab)
de générateurs de variables distribuées suivant la loi gaussienne, mais ce n'est pas toujours le
cas. Il est donc important d'être en mesure d'écrire un code permettant de générer une variable
aléatoire gaussienne. Dans cet exercice nous présentons une méthode classique due à Box et
Muller (1958) permettant de générer deux réalisations indépendantes de la loi $\mathcal N(0,1)$.

1. **Question préliminaire.** Soit $X_1$ et $X_2$ deux variables aléatoires indépendantes de
   loi $\mathcal N(0,1)$ ; on pose $Z = X_1^2 + X_2^2$. On demande de montrer que $Z$ est
   distribuée suivant une loi exponentielle de moyenne $1/\lambda$ avec $\lambda = 1/2$.
   Pour ce faire donner l'expression de $P(Z \ge z)$. Exprimer $P(Z \ge z)$ comme une intégrale
   double des variables $(x_1, x_2)$ faisant intervenir les densités de $X_1$ et de $X_2$ et
   procéder au changement de variable $(x_1 = r\cos\theta,\ x_2 = r\sin\theta)$ pour se ramener
   à une intégrale en $(r, \theta)$.
   On doit trouver $P(Z \ge z) = \exp(-2z)\mathbb 1_{\mathbb R^+}(z) + \mathbb 1_{\mathbb R^{*-}}(z)$,
   fonction de répartition complémentaire de la loi $\mathcal E(\lambda = 1/2)$.
   > ⚠️ **Coquille** : avec $\lambda = 1/2$, c'est $\exp(-z/2)$ (le calcul le confirme).
2. Soit $X_1$ et $X_2$ deux variables aléatoires indépendantes de loi $\mathcal N(0,1)$ et soit
   $(r, \theta)$ les coordonnées polaires du point de coordonnées cartésiennes $(X_1, X_2)$.
   Montrer en utilisant la question précédente que $r^2$ suit une loi $\mathcal E(1/2)$ et
   justifier que $\theta$ est distribuée suivant une loi uniforme sur $[0, 2\pi]$.
3. En déduire une méthode de génération de deux variables aléatoires indépendantes et de loi
   $\mathcal N(0,1)$.
4. Rappeler la transformation linéaire permettant d'obtenir une variable aléatoire
   $Y \sim \mathcal N(\mu, \sigma^2)$ à partir d'une variable aléatoire $X \sim \mathcal N(0,1)$.
   Générer suivant la méthode de Box et Muller $T = 10000$ réalisations indépendantes de la loi
   $\mathcal N(\mu = 5, \sigma^2 = 4)$.
5. Vérifier que la moyenne et la variance de l'échantillon obtenu sont cohérents avec les
   valeurs prescrites et représenter un histogramme de l'échantillon généré.

*(La fin de la page 15 — « Fonctions Matlab à utiliser » — est masquée sur la photo ; on y
devine `rand` pour la génération uniforme.)*
