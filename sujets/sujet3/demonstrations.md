# Sujet 3 — Démonstrations

Notations : $h(x) = x^2 + 3x\cos x$ sur $I = [-8\pi, 8\pi]$ ; $x^\star \approx -0{,}637$ désigne le
minimum **global** de $h$ sur $I$, et $\bar x \approx 8{,}814$ le minimum **local** du bassin de
$x_0 = 7{,}5$. Les valeurs numériques viennent de `s3_1_recuit_simule.ipynb` (graine 2026)
ou d'un calcul exact (`scipy.optimize.brentq` sur $h'$).

---

<a id="q0"></a>

## Q0 — Maximiser, c'est minimiser l'opposé

Pour tous $x, x_M$ : $h(x) \le h(x_M) \iff -h(x) \ge -h(x_M)$. Donc $x_M$ maximise $h$ si et
seulement s'il minimise $-h$ :
```math
\boxed{\arg\max h = \arg\min(-h), \qquad \max h = -\min(-h).}
```
L'énoncé écrit « $h = -h$ » : il faut lire « on remplace $h$ par $\tilde h = -h$ ».

---

<a id="q1"></a>

## Q1 — La fonction $h$ et ses extrema

**Dérivées.** Par la formule du produit $(uv)' = u'v + uv'$ avec $u = 3x$, $v = \cos x$ :
```math
\boxed{h'(x) = 2x + 3\cos x - 3x\sin x,\qquad h''(x) = 2 - 6\sin x - 3x\cos x.}
```

**Pourquoi tant d'extrema ?** Le terme $3x\cos x$ oscille avec une amplitude $3|x|$ qui grandit,
alors que la courbure de $x^2$ reste égale à 2. Dans $h''$, le terme $-3x\cos x$ dépasse 2 en
valeur absolue dès que $|x|$ n'est pas petit. Exemple : $h''(0) = 2 > 0$ mais
$h''(2\pi) = 2 - 6\pi \approx -16{,}8 < 0$. $h''$ change de signe, $h$ **n'est pas convexe**, et la
théorie « gradient → unique minimum » ne s'applique pas.

Sur $I$, $h'$ s'annule 17 fois : **9 minima locaux** et 8 maxima locaux (calcul numérique).

**Où est le minimum global ?** Minoration : $\cos x \ge -1$ et $\cos x \le 1$ donnent
$3x\cos x \ge -3|x|$, donc
```math
h(x) \ge x^2 - 3|x| = |x|\,(|x| - 3) > 0 \quad \text{pour } |x| > 3.
```
Or $h(-0{,}637) \approx -1{,}130 < 0$. Le minimum global est donc **forcément dans $]-3, 3[$**.
Il n'y a là que deux minima locaux :

| minimum local | $h$ | statut |
|---|---|---|
| $x \approx -0{,}6371$ | $-1{,}1305$ | **global** |
| $x \approx 2{,}8051$ | $-0{,}0748$ | local, piège le plus proche en valeur |

Contrôle : la minoration donne aussi $h \ge \min_t (t^2 - 3t) = -9/4$, et $-1{,}13 \ge -2{,}25$. ✔

**Le point de départ.** $x_0 = 7{,}5$ est entre les maxima locaux $7{,}143$ et $13{,}368$ : c'est
le bassin d'attraction du minimum local $x \approx 8{,}8137$, où $h \approx 56{,}03$, très loin du
minimum global.

**Remarques utiles à l'oral.**
- *Pourquoi ne pas lire directement le minimum sur la grille ?* En 1D, `min(h_n)` sur 5000 points
  donne le minimum global à $16\pi/5000 \approx 0{,}01$ près : c'est la « force brute ». Elle
  devient impossible en grande dimension ($5000^d$ points). Les deux algorithmes du TD servent
  dans ce cas ; la dimension 1 sert seulement à **voir** ce qu'ils font.
- $h$ n'est pas paire : $h(-x) = x^2 - 3x\cos x \neq h(x)$, d'où des minima non symétriques.

---

<a id="q2"></a>

## Q2 — Gradient simple

**Numérotation.** Avec $\alpha_n = 0{,}025/n$, le premier pas ne peut pas utiliser
$\alpha_0 = 0{,}025/0$ : on écrit $x_n = x_{n-1} - \alpha_n h'(x_{n-1})$ pour $n \ge 1$ (c'est ce que
fait le code). Même convention pour le recuit : le pas $n$ utilise $T_n$.

**Pourquoi $h$ diminue.** Taylor-Lagrange à l'ordre 2, avec $g = h'(x)$ et $M$ un majorant de
$h''$ sur le segment $[x, x - \alpha g]$ :
```math
h(x - \alpha g) = h(x) - \alpha g^2 + \tfrac{\alpha^2 g^2}{2} h''(\xi) \le h(x) - \alpha g^2\Big(1 - \frac{\alpha M}{2}\Big).
```
Sur $[7{,}5 ; \bar x]$, $\max h'' = h''(\bar x) \approx 20{,}2$ et $\alpha_n \le 0{,}025$, donc
$\alpha_n M/2 \le 0{,}25 < 1$ : $h$ diminue **strictement** à chaque pas tant que $h' \ne 0$ (et le
notebook le vérifie).
En $x_0 = 7{,}5$, $h'(7{,}5) \approx -5{,}07 < 0$ : on avance vers la droite, vers $8{,}81$.

**Rôle des deux conditions sur le pas.**
- $\sum \alpha_n = +\infty$ : sinon le déplacement total est borné par
  $\sum \alpha_n |h'(x_n)| \le \sup|h'| \sum \alpha_n < \infty$ et l'algorithme peut s'arrêter
  **avant** d'atteindre le minimum.
- $\sum \alpha_n^2 < +\infty$ : les pas tendent vers 0 assez vite pour que la suite ne puisse pas
  osciller indéfiniment autour du minimum (condition surtout cruciale quand le gradient est
  bruité : gradient stochastique).
- Avec $\alpha_n = 0{,}025/n$ : $\sum 1/n = +\infty$ (série harmonique) et
  $\sum 1/n^2 = \pi^2/6 < \infty$. ✔

**Le gradient reste dans son bassin.** Posons $\varphi_n(x) = x - \alpha_n h'(x)$, de sorte que
$x_n = \varphi_n(x_{n-1})$. Sur $[7{,}5 ; \bar x]$ :
- $\varphi_n'(x) = 1 - \alpha_n h''(x) \ge 1 - 0{,}025 \times 20{,}2 = 0{,}495 > 0$ : $\varphi_n$ est
  croissante ;
- $\varphi_n(\bar x) = \bar x$ car $h'(\bar x) = 0$.

Donc $x_{n-1} < \bar x \Rightarrow x_n = \varphi_n(x_{n-1}) < \varphi_n(\bar x) = \bar x$ : on ne
dépasse jamais $\bar x$. Comme $h' < 0$ sur $]7{,}14 ; \bar x[$, $x_n > x_{n-1}$ : la suite est
**croissante et majorée**, donc converge vers une limite $\ell \le \bar x$. Si $h'(\ell) \ne 0$, les
pas vaudraient $\approx \alpha_n |h'(\ell)|$ et leur somme divergerait ($\sum\alpha_n = \infty$),
contradiction : $h'(\ell) = 0$, donc $\ell = \bar x$, le minimum **local**.

**Vitesse de convergence.** Près de $\bar x$ : $h'(x) \approx h''(\bar x)(x - \bar x)$. L'erreur
$e_n = x_n - \bar x$ vérifie donc
```math
e_{n+1} \approx \Big(1 - \frac{c}{n}\Big) e_n, \qquad c = 0{,}025\, h''(\bar x).
```
Comme $\ln \prod_{k \le n} (1 - c/k) \approx -c \sum_{k\le n} 1/k \approx -c \ln n$, on obtient
```math
\boxed{|e_n| \approx C\, n^{-c}}\quad (C \text{ constante}).
```
Ici $h''(\bar x) = h''(8{,}8137) \approx 20{,}21$, donc $c \approx 0{,}505$ : l'erreur décroît comme
$1/\sqrt n$. Vérification numérique : $|e_{1000}| \approx 0{,}153$, $|e_{10^4}| \approx 0{,}051$,
$|e_{10^5}| \approx 0{,}016$, soit un facteur $\approx 3{,}1 \approx \sqrt{10}$ par décade. ✔

C'est **lent** (convergence sous-linéaire). Avec un pas constant $\alpha$ assez petit, on aurait
$e_{n+1} \approx (1 - \alpha h'') e_n$, une convergence géométrique, bien plus rapide.

---

<a id="q3"></a>

## Q3 — Recuit simulé

**La règle d'acceptation (Metropolis).** Probabilité d'accepter $z$ :
```math
p_n = \min\big(1,\ e^{-\Delta h_n / T_n}\big), \qquad \Delta h_n = h(z) - h(x_n).
```
- Si $\Delta h_n \le 0$ : $p_n = 1$ (on descend toujours).
- Si $\Delta h_n > 0$ : $p_n \in\, ]0, 1[$, plus petit si la dégradation $\Delta h_n$ est grande
  ou si $T_n$ est petit.
- $T$ grand : $p \approx 1$, marche aléatoire qui **explore** tout l'intervalle.
- $T \to 0$ : $p \to 0$ pour toute montée, on ne fait plus que **descendre**.

En pratique : tirer $U \sim \mathcal U[0,1]$ et accepter si $U < e^{-\Delta h_n/T_n}$, car
$P(U < p) = p$ (fonction de répartition de $\mathcal U[0,1]$, comme au sujet 1).

**Ordres de grandeur avec l'énoncé** ($T_n = 500 \times 0{,}99^n$) : $T_n = 1$ pour
$n = \ln 500 / \ln(1/0{,}99) \approx 618$, et $T_{1000} \approx 0{,}022$. Au début, un saut de
$\pm\pi/2$ coûte au plus $\approx 118 \times \pi/2 \approx 185$, accepté avec probabilité
$\ge e^{-185/500} \approx 0{,}69$ : le taux d'acceptation est élevé.

**Pourquoi ça vise le minimum global : la loi de Boltzmann.** À température **fixée** $T$, la
proposition est symétrique ($g(z \mid x) = 1/\pi$ si $|z - x| \le \pi/2$, idem pour
$g(x \mid z)$). Posons $\mu_T(x) \propto e^{-h(x)/T}$ sur $I$ (loi de Boltzmann ; on évite la lettre
$\pi$, déjà prise). Pour $x \neq y$ dans $I$ avec $|x - y| \le \pi/2$ :
```math
\mu_T(x)\, g(y\mid x)\, \min\big(1, e^{-(h(y)-h(x))/T}\big) = \frac1\pi \min\big(\mu_T(x), \mu_T(y)\big),
```
expression symétrique en $(x, y)$ : c'est l'**équilibre détaillé**. La chaîne de Markov
$(x_n)$ admet donc $\mu_T$ comme loi stationnaire (refuser les $z$ hors de $I$ ne casse pas la
symétrie). Or
```math
\frac{\mu_T(x)}{\mu_T(x^\star)} = e^{-(h(x) - h(x^\star))/T} \xrightarrow[T \to 0]{} 0 \quad \text{si } h(x) > h(x^\star) :
```
quand $T \to 0$, $\mu_T$ se concentre sur les minima **globaux**. Le recuit suit ces lois en
refroidissant : il faut refroidir **assez lentement** pour que la chaîne ait le temps de se
rééquilibrer.

**La garantie théorique.** Résultat classique (Hajek, 1988, espace d'états **fini** ; il existe
des analogues continus) : avec $T_n = c / \ln n$, $P(x_n \in \arg\min h) \to 1$ si et seulement si
$c \ge d^\star$, où $d^\star$ est la profondeur du minimum local non global le plus profond
(hauteur à remonter pour en sortir vers un point plus bas). C'est une convergence **en
probabilité**, pas presque sûre : même avec ce refroidissement, la chaîne ressort infiniment souvent
du voisinage du minimum global. Profondeurs sur $I$, le long d'un chemin continu (petits pas) :

| minimum local | $h$ | col à franchir | profondeur |
|---|---|---|---|
| $2{,}805$ | $-0{,}075$ | max en $1{,}227$ ($h = 2{,}746$) | $2{,}82$ |
| $8{,}814$ | $56{,}03$ | max en $7{,}143$ ($h = 65{,}01$) | $8{,}98$ |
| $-24{,}44$ (bord gauche) | $540{,}9$ | max en $-22{,}76$ ($h = 567{,}1$) | $26{,}2$ |

Avec des sauts de $\pm\pi/2$, la chaîne enjambe une partie des cols : en cherchant, sur une grille
de 8001 points, le chemin à sauts $\le \pi/2$ dont le point le plus haut est le plus bas possible,
on trouve des profondeurs effectives $\approx 12{,}3$ (pour $-24{,}44$) et $\approx 1{,}5$ (pour
$2{,}805$). Dans tous les cas il faudrait $c \gtrsim 12$, soit $T_{1000} \gtrsim 1{,}8$, contre
$0{,}022$ avec l'énoncé : un refroidissement logarithmique est beaucoup trop lent en pratique.

**Pourquoi l'affirmation de l'énoncé est fausse (gel).** Avec $T_n = T_0\alpha^n$, la probabilité de
franchir un col de hauteur $d > 0$ à l'itération $n$ est au plus de l'ordre de $e^{-d/T_n}$, et
```math
\sum_n e^{-d/T_n} = \sum_n e^{-d\,\alpha^{-n}/T_0} < \infty
```
(décroissance doublement exponentielle ; pour $d = 1{,}5$, le reste au-delà de $n = 1000$ vaut
moins de $10^{-30}$). Par Borel-Cantelli, presque sûrement la chaîne ne franchit plus qu'un nombre
**fini** de cols : elle gèle dans un bassin aléatoire. La proportion de lancers piégés (25,9 %)
est donc la proportion **limite**, pas un effet d'un $N$ trop petit. « Ce choix garantit la
convergence presque sûre » est faux.

**Pourquoi environ un lancer sur quatre finit en $2{,}805$ (intuition).** Les deux minima les plus
bas ne diffèrent que de $\Delta \approx 1{,}06$. Quand $T$ passe sous $\approx 1$ (vers
$n \approx 620$), les passages du col en $1{,}227$ deviennent rares : la chaîne « gèle » dans le
bassin où elle se trouve. À $T = 1$, la masse de Boltzmann du bassin de $2{,}805$ (calculée par
intégration numérique de $e^{-h/T}$) vaut $\approx 0{,}25$ : c'est l'ordre de grandeur de la
proportion d'échecs observée.

---

<a id="q4"></a>

## Q4 — Comparaison (synthèse)

| critère | gradient simple | recuit simulé |
|---|---|---|
| nature | déterministe | stochastique (chaîne de Markov) |
| information utilisée | $h$ **et** $h'$ | $h$ seulement (pas de dérivée) |
| garantie | minimum **local** du bassin de $x_0$ ; global garanti si $h$ convexe (ou si $x_0$ est dans le bassin du global) | global en probabilité si $T_n = c/\ln n$, $c \ge d^\star$ ; aucune avec $T_n = T_0\alpha^n$ |
| dépend de $x_0$ | oui, entièrement | peu (l'exploration initiale fait oublier $x_0$) |
| vitesse | $n^{-c}$ ici ($c \approx 0{,}5$), géométrique avec pas constant | lente, réglage $T_0$, $\alpha$, largeur |
| coût par itération | 1 évaluation de $h'$ | 1 évaluation de $h$ + 2 tirages uniformes |
| compréhension / mise en œuvre | simple, 1 paramètre (le pas) | plus subtile, 3 paramètres, résultat aléatoire à évaluer sur plusieurs lancers |

Combinaison courante : recuit (exploration), puis gradient depuis le meilleur point trouvé
(affinage local rapide), ou gradient lancé depuis plusieurs $x_0$ (*multistart*).
