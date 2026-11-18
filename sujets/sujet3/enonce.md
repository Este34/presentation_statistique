# Sujet 3 — Un algorithme d'optimisation stochastique : le recuit simulé

> Transcription de l'énoncé papier (pages 20-22). Les fonctions Matlab citées sont traduites
> en Python dans [matlab_python.md](matlab_python.md).

Dans ce STP nous comparons deux algorithmes d'optimisation : le premier algorithme est un
algorithme déterministe, l'algorithme du gradient déterministe ; le second est un algorithme
stochastique, l'algorithme du recuit simulé.

On désire minimiser une fonction $x \mapsto h(x)$. Un problème de maximisation se ramènerait à
un problème de minimisation en faisant la transformation $h = -h$.

> ⚠️ **Coquille** : écrire $\tilde h = -h$ (on minimise $\tilde h$) ; « $h = -h$ » n'a pas de
> sens comme égalité. Maximiser $h$ revient à minimiser $-h$, car $\max h = -\min(-h)$, atteint
> aux mêmes points.

## Algorithme du gradient simple

L'algorithme du gradient simple est le suivant :

1. définir $x_0$ ;
2. répéter $x_{n+1} = x_n - \alpha_n \nabla h(x_n)$ sur $N$ itérations (ou tant qu'un certain
   critère d'arrêt n'est pas satisfait),

avec $\nabla h(x)$ le gradient de $h$ au point $x$ et avec $\alpha_n$ un pas vérifiant
$\sum \alpha_n = +\infty$ et $\sum \alpha_n^2 < +\infty$ (par exemple on peut prendre
$\alpha_n = O(1/n)$).

> ⚠️ **Coquille** : « $\alpha_n = O(1/n)$ » ne garantit pas $\sum\alpha_n = +\infty$ ($1/n^2$ est un
> $O(1/n)$ et sa série converge). Il faut $\alpha_n$ proportionnel à $1/n$ (par exemple $c/n$).

Le principe de l'algorithme du gradient simple est de parcourir la surface $x \mapsto h(x)$ dans
la direction de plus grande pente jusqu'à rencontrer un extrêmum local de $h$.

Sous les conditions sur $\alpha_n$ énoncées ci-dessus l'algorithme du gradient simple converge
vers l'unique minimum de $h$ dans le cas où $h$ est convexe. Dans le cas général l'algorithme du
gradient simple converge vers un minimum **local** mais pas nécessairement **global** de $h$.

Dans le cas général le point $x^* = \lim_n x_n$ vers lequel l'algorithme converge dépend donc de
l'initialisation $x_0$. Dans beaucoup d'applications un extrêmum local de la fonction à optimiser
ne suffit pas ; une solution est alors d'avoir recours à l'algorithme du recuit simulé.

## Algorithme du recuit simulé

Cet algorithme stochastique permet sous certaines conditions de sortir des bassins d'attraction
des extrema locaux de la fonction à optimiser. À chaque itération on réactualise $x_n$ de la
façon suivante :

1. générer $z$ suivant une distribution instrumentale $g_n(z)$ ;
2. si $h(z) \le h(x_n)$ accepter $x_{n+1} = z$ avec une probabilité 1 ; si $h(z) > h(x_n)$
   accepter $x_{n+1} = z$ avec une probabilité $\exp(-\Delta h_n / T_n)$,
   $\Delta h_n = h(z) - h(x_n)$, et faire $x_{n+1} = x_n$ sinon.

Le principe est donc de générer $z$ suivant une distribution généralement centrée autour de
$x_n$. Si le choix $x_{n+1} = z$ permet de diminuer la valeur de la fonction $h$ à minimiser on
pose $x_{n+1} = z$ ; si au contraire il l'augmente on accepte tout de même $x_{n+1} = z$ avec une
probabilité d'autant plus faible que croît le nombre des itérations et que la dégradation
$h(z) - h(x_n)$ est élevée.

La suite $(T_n)_n$ est une suite décroissante de « températures ». Sous certaines conditions sur
$T_n$ l'algorithme du recuit simulé converge presque sûrement vers l'ensemble des extrema globaux
de $h$.

> ⚠️ **Coquille / à corriger** : il s'agit des **minima** globaux (on minimise). Et le résultat
> classique (Hajek, 1988, espace fini) donne une convergence **en probabilité**, pas presque sûre,
> avec une décroissance **logarithmique** $T_n = c/\ln n$, $c$ assez grand ; voir
> [demonstrations.md](demonstrations.md#q3).

On désire minimiser la fonction $h(x) = x^2 + 3x\cos(x)$ sur l'intervalle $[-8\pi, +8\pi]$. Sur
l'intervalle $[-8\pi, +8\pi]$ cette fonction présente un certain nombre d'extrema locaux. Nous
allons comparer le résultat de l'algorithme du gradient simple et de l'algorithme du recuit
simulé pour un même point d'initialisation $x_0 = 7.5$ choisi dans le bassin d'attraction d'un
extrêmum local mais non global de $h$.

1. Représenter la fonction $h(x)$ sur l'intervalle $[-8\pi, +8\pi]$.
   Indication : discrétiser l'intervalle $[-8\pi, +8\pi]$ sur par exemple 5000 points
   $y_n = -8\pi + 16\pi \frac{n-1}{5000}$, $1 \le n \le 5000$ et calculer la valeur
   $h_n = h(y_n)$ prise par la fonction $h$ en chacun des points $y_n$.
   Remarquer que sur cet intervalle $h$ présente un certain nombre d'extrema locaux non globaux
   vers lesquels l'algorithme du gradient simple est susceptible de converger.

   > ⚠️ **Coquille** : avec $\frac{n-1}{5000}$, le dernier point est
   > $y_{5000} = 8\pi - 16\pi/5000$ : la borne $+8\pi$ n'est jamais atteinte. Pour couvrir
   > exactement l'intervalle, diviser par $4999$ (c'est ce que fait `np.linspace(-8π, 8π, 5000)`,
   > comme `linspace` en Matlab). Aussi : « discrétiser l'intervalle ~~sur~~ par exemple ».

2. **Algorithme du gradient simple** : implémenter l'algorithme du gradient simple
   ```math
   x_{n+1} = x_n - \alpha_n h'(x_n) \qquad (1)
   ```
   On conseille de prendre pour le pas $\alpha_n = \frac{0.025}{n}$. Faire suffisamment
   d'itérations pour observer la convergence de l'algorithme vers un extrêmum local de $h$ (de
   l'ordre de 1000 itérations pour ce choix du pas $\alpha_n$). Visualiser sur le graphe
   $x \to h(x)$ la convergence de la suite $(x_n)_n$ vers un minimum local de $h$.

   > ⚠️ **Indice** : avec $x_0$ donné, (1) utiliserait $\alpha_0 = 0{,}025/0$, non défini. On
   > numérote donc $x_n = x_{n-1} - \alpha_n h'(x_{n-1})$ pour $n \ge 1$ (même convention pour
   > $T_n$ au recuit).

3. **Algorithme du recuit simulé.** On choisit comme distribution instrumentale $g_n(z)$ la
   distribution uniforme sur $[x_n - \frac{\pi}{2}, x_n + \frac{\pi}{2}]$. On conseille d'autre
   part le choix suivant pour la suite des températures $T_n = T_0\alpha^n$ avec $T_0 = 500$ et
   $\alpha = 0.99$ ; pour la fonction $h$ ce choix garantit la convergence presque sûre de $x_n$
   vers l'ensemble des minima globaux de $h$. D'autre part $\alpha$ et $T_0$ ont été choisis de
   façon à avoir à la fois un taux d'acceptation élevé lors des premières itérations et une
   convergence relativement rapide de l'algorithme.
   De la même façon que pour l'algorithme du gradient simple visualiser sur le graphe
   $x \to h(x)$ la convergence de $x_n$ vers un minimum cette fois-ci global de $h$.

   > ⚠️ **Notation** : la lettre $\alpha$ sert deux fois (pas $\alpha_n$ du gradient et facteur
   > de refroidissement $\alpha = 0.99$). Ce sont deux paramètres différents ; dans le code :
   > `pas(n)` et `alpha`.
   >
   > ⚠️ **Faux** : « ce choix garantit la convergence presque sûre ». Avec $T_n = T_0\alpha^n$,
   > $\sum_n e^{-d/T_n} < \infty$ pour toute hauteur de col $d > 0$ : par Borel-Cantelli, la chaîne
   > finit par geler dans un bassin aléatoire. L'expérience le confirme : sur 1000 lancers, 25,9 %
   > finissent dans le minimum local $2{,}805$ (notebook, Q4).

4. Commenter. Comparer les deux méthodes en termes de garanties de convergence, de vitesses de
   convergence, de complexité de compréhension, de complexité de mise en œuvre…

**Fonctions Matlab à utiliser** : boucles `for` ; génération d'une variable uniformément
distribuée sur $[0,1]$ : `rand` ; minimum, maximum d'un vecteur, d'une matrice : fonctions `min`
et `max` ; test logique : fonction `if` ; pour les représentations graphiques : fonctions `plot`,
`hold on`, `hold off`…
