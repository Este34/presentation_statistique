# Sujet 4 · Questions probables du jury

Niveaux : **N1** définition / restitution · **N2** démonstration / calcul · **N3** « et si… », recul.
Les questions marquées **(hors rendu)** portent sur des notions retirées du PDF : si le jury les pose,
réponds avec l'idée simple donnée, sans entrer dans la preuve.
Chiffres : notebook `s4_1_file_mm1.ipynb` (graine 2026), voir [fiche_revision.md](fiche_revision.md).

---

## Loi exponentielle (A)

**1. (N1) Donnez la densité, la fonction de répartition et la moyenne de $\mathcal E(\lambda)$.**
*Attendu* : $f(x) = \lambda e^{-\lambda x}$ pour $x \ge 0$ ; $F(x) = 1 - e^{-\lambda x}$ ;
$E[X] = 1/\lambda$. Unité : si $\lambda$ est un nombre d'événements par seconde, $1/\lambda$ est en
secondes. *Piège* : dire que la moyenne vaut $\lambda$.

**2. (N2) Montrez que la moyenne et l'écart-type sont égaux.**
*Attendu* : IPP, $E[X] = 1/\lambda$, $E[X^2] = 2/\lambda^2$, $\operatorname{Var}X = 1/\lambda^2$
(König-Huygens), donc $\sigma = 1/\lambda$. Contrôle : $0{,}498$ et $0{,}499$ pour $\lambda = 2$.
*Piège* : oublier de soustraire $E[X]^2$, ou confondre variance et écart-type.

**3. (N1) Que veut dire « sans mémoire » ? Donnez un exemple concret.**
*Attendu* : $P(X \ge x + t \mid X \ge x) = P(X \ge t)$ : ce qui reste à attendre ne dépend pas de
ce qu'on a déjà attendu. Exemple : un client servi depuis 10 s a encore un temps restant
$\mathcal E(\mu)$, comme s'il venait de commencer.

**4. (N2) Démontrez l'absence de mémoire.**
*Attendu* : $\{X \ge x + t\} \subset \{X \ge x\}$, donc
$P(\cdot \mid \cdot) = G(x+t)/G(x) = e^{-\lambda t}$. *Piège* : oublier de justifier
l'intersection (il faut $t \ge 0$) ou que $G(x) > 0$.

**5. (N3) Pourquoi est-ce la seule loi sans mémoire ? Quelles hypothèses ?**
*Attendu* : $G(x+t) = G(x)G(t)$, $\ln G$ additive et monotone, donc linéaire (rationnels puis
densité). Hypothèses : $G > 0$ et $(*)$ pour **tous** $x, t \ge 0$ réels (la loi géométrique n'est
sans mémoire que pour des $x, t$ entiers). *Piège* : « par continuité » sans dire d'où vient la
continuité (ici la monotonie suffit).

**6. (N3) Une ampoule réelle est-elle sans mémoire ?**
*Attendu* : non, elle s'use : sa durée de vie restante diminue avec l'âge (comme Erlang(2) dans le
notebook : $0{,}735$ à l'âge 0 contre $0{,}487$ à l'âge 1). L'exponentielle convient aux pannes
« accidentelles » à taux constant. Question bonus, hors programme strict : loi de Weibull.

## Processus de Poisson (B) et simulation

**7. (N1) Qu'est-ce qu'un processus de Poisson d'intensité $\lambda$ ?**
*Attendu* : des points sur $\mathbb R^+$ dont les écarts successifs sont indépendants de loi
$\mathcal E(\lambda)$ ; $\lambda$ = nombre moyen de points par unité de temps.

**8. (N2) Pourquoi la densité d'une somme de deux variables indépendantes est-elle une convolution ?**
*Attendu* : densité jointe = produit (indépendance), on intègre sur $\{x_1 + x_2 \le z\}$, changement
de variable $s = x_1 + x_2$ puis Fubini-Tonelli. *Piège* : oublier l'indépendance (sans elle, la
densité jointe n'est pas le produit).

**9. (N2) Calculez la densité de $T_2$.**
*Attendu* : $\int_0^x \lambda e^{-\lambda u}\lambda e^{-\lambda(x-u)}du = \lambda^2 x e^{-\lambda x}$ : les
indicatrices limitent $u$ à $[0, x]$. *Piège* : intégrer sur $[0, \infty[$.

**10. (N2) Comment passe-t-on de $T_k$ à $N_t$ ?**
*Attendu* : $\{N_t = k\} = \{T_k \le t < T_{k+1}\}$, donc $P(N_t = k) = F_k(t) - F_{k+1}(t)$
(inclusion $\{T_{k+1} \le t\} \subset \{T_k \le t\}$), puis IPP. *Piège* : écrire
$P(T_k \le t)P(T_{k+1} > t)$ (les deux événements ne sont pas indépendants).

**11. (N2) Montrez que $-\frac1\lambda\ln U$ suit $\mathcal E(\lambda)$.**
*Attendu* : $P(X \ge x) = P(U \le e^{-\lambda x}) = e^{-\lambda x}$ (exp croissante, $P(U \le u) = u$).
Lien avec la méthode d'inversion du sujet 1. *Piège* : $\ln U$ négatif, d'où le signe moins ; et
$\ln 0$ : utiliser $1 - U$.

**12. (N2) Décrivez l'algorithme qui simule $\mathcal P(\lambda)$. Combien coûte-t-il ?**
*Attendu* : additionner des $\mathcal E(\lambda)$ jusqu'à dépasser 1 et compter : $N_1$ d'un processus
de Poisson. $N + 1$ uniformes, soit $\lambda + 1$ en moyenne. Variante de Knuth : produit
d'uniformes $\ge e^{-\lambda}$. Contrôle : moyenne $3{,}99$, variance $3{,}96$ pour $\lambda = 4$.

**13. (N3) Et si $\lambda = 10^4$ ?**
*Attendu* : $10^4$ uniformes par tirage, trop lent. On utilise une autre méthode (rejet, ou
approximation normale $\mathcal N(\lambda, \lambda)$ par le TCL). Question bonus, hors programme strict.

## La file M/M/1

**14. (N1) Que signifie M/M/1 ? Qu'est-ce que $\rho$ ?**
*Attendu* : arrivées poissoniennes (M), services exponentiels (M), un serveur (1), FIFO.
$\rho = \lambda/\mu$ = temps de service moyen / temps moyen entre deux arrivées = fraction du temps
où le serveur travaille. *Piège* : $\rho = \mu/\lambda$ (la coquille de l'énoncé).

**15. (N2) Expliquez la récurrence $L_{n+1} = (L_n + 1 - A_n)^+$.**
*Attendu* : après l'arrivée $n$ il y a $L_n + 1$ clients ; pendant $[T_n, T_{n+1}[$, $A_n$ services
possibles en font partir $\min(A_n, L_n + 1)$ : on ne peut pas faire partir plus de clients qu'il
n'y en a. Exemple de la figure : $A_3 = 6$ pour 1 client, 5 services perdus.

**16. (N3) Pourquoi a-t-on le droit d'utiliser un processus de Poisson $N(t)$ pour les départs, même quand la file se vide ?**
*Attendu* : absence de mémoire : pendant une période d'activité, la fin du service en cours arrive
au taux $\mu$ quel que soit le temps déjà passé. On peut donc tirer les « services possibles » à
l'avance et ignorer ceux qui tombent quand la file est vide : même loi pour $L(t)$. Validé par une
simulation FIFO directe (mêmes chiffres). *Piège* : dire que $N(t)$ compte les départs (il compte
les départs **possibles**).

**17. (N2) Quelle est la loi de $A_n$ ?**
*Attendu* : sachant l'écart $s$, $\mathcal P(\mu s)$ ; en intégrant contre $\lambda e^{-\lambda s}$ :
$P(A_n = k) = \frac{\lambda}{\lambda+\mu}\big(\frac{\mu}{\lambda+\mu}\big)^k$, géométrique, de moyenne
$\mu/\lambda$. Intuition : course entre l'horloge des arrivées et celle des services.

**18. (N1) Décrivez votre algorithme de simulation.**
*Attendu* : boucle : tirer l'écart $s \sim \mathcal E(\lambda)$ par inversion, tirer
$A \sim \mathcal P(\mu s)$ par comptage, $l \leftarrow \max(0, l + 1 - A)$, $t \leftarrow t + s$,
jusqu'à 300 s. File vide au départ : $L_1 = 0$.

**19. (N2) Comment avez-vous vérifié que l'algorithme est juste ?**
*Attendu* : la loi simulée de $L_n$ suit $(1-\rho)\rho^k$ (une droite en échelle log) et les
indicateurs collent à la théorie à quelques pour cent près ($5{,}13$ pour 5, $0{,}159$ pour $0{,}167$,
$0{,}338$ pour $0{,}335$) ; plus des tests automatiques (pytest). Bonus (hors rendu) : deux autres
simulations du même modèle, dans `src/stats_td/files_attente.py`, donnent les mêmes valeurs.

**20. (N2) Pourquoi la file croît-elle indéfiniment si $\rho > 1$ ? À quelle vitesse ?**
*Attendu* : $L_n \ge S_n = \sum_{k<n}(1 - A_k)$ et $S_n/n \to 1 - 1/\rho > 0$ (loi forte des grands
nombres). En temps : $(\lambda - \mu)\,t$. Mesuré : 1120 clients après 60 s à $\rho = 1{,}2$ (pente
$19{,}7$/s pour 20). *Piège* : dire « elle croît car il arrive plus de clients » sans quantifier.

**21. (N3) Et si $\rho = 1$ exactement ?**
*Attendu* : marche aléatoire sans dérive, récurrente **nulle** : la file revient à 0 mais de plus en
plus rarement et croît comme $\sqrt n$. Pas de régime stationnaire ($\rho/(1-\rho)$ infini).

**22. (N2) Que veut dire « la file se stationnarise » ?**
*Attendu* : la **loi** de $L_n$ se stabilise (vers $(1-\rho)\rho^k$), pas la trajectoire, qui continue
de fluctuer : la file revient sans cesse à 0 et la moyenne cumulée se stabilise ($1{,}49$ pour $1{,}5$
à $\rho = 0{,}6$). *Piège* : dire que $L_n$ devient constant. Bonus (hors rendu) : chaîne de Markov
récurrente positive, théorème ergodique.

**23. (N3, hors rendu) D'où vient $(1-\rho)\rho^k$ ?**
*Attendu* : l'énoncé demande de le **vérifier par simulation**, c'est ce que j'ai fait (la loi simulée
suit la droite en échelle log). Pour aller plus loin : on vérifie que cette loi se reproduit par la
récurrence, grâce à l'identité $\rho q = p$.

**24. (N2) Calculez $E[L]$, $\operatorname{Var}L$, $P(\text{serveur libre})$, $P(L > 5)$ pour $\rho = 5/6$.**
*Attendu* : $\frac{\rho}{1-\rho} = 5$ ; $\frac{\rho}{(1-\rho)^2} = 30$ ; $1 - \rho = 1/6$ ;
$\rho^6 = 0{,}335$. Simulé : $5{,}13$ ; $32{,}5$ ; $0{,}159$ ; $0{,}338$.
*Piège* : $P(L > 5) = \rho^5$ (c'est $P(L \ge 5)$).

**25. (N3) Vos valeurs simulées ne tombent pas exactement sur la théorie. Est-ce grave ?**
*Attendu* : non, une simulation est aléatoire : sur 5 minutes, des écarts de quelques pour cent sont
normaux ($+2{,}6$ % sur la moyenne). La variance s'écarte le plus ($+8{,}4$ %) car elle dépend des rares
longues files. *Piège* : vouloir quantifier avec $\hat\sigma/\sqrt n$ : les $L_n$ successifs sont
corrélés, cette formule serait trop optimiste (bonus hors rendu : méthode des lots).

**26. (N3) La file part vide. Est-ce un problème ?**
*Attendu* : la loi géométrique est la loi **limite**. Le régime transitoire dure quelques secondes
(temps de relaxation de l'ordre de la seconde) ; sur 300 s l'effet est faible : sans les 10
premières secondes, moyenne $5{,}06$ au lieu de $5{,}13$ : presque pareil.

**27. (N3) La loi de $L_n$ (vue par les arrivants) est-elle la même que celle de $L(t)$ à un instant quelconque ?**
*Attendu* : oui pour des arrivées poissoniennes : propriété PASTA (*Poisson Arrivals See Time
Averages*). Question bonus, hors programme strict.

**28. (N3, hors rendu) Combien de temps un client passe-t-il en moyenne dans le système ?**
*Attendu* : $L$ services devant lui plus le sien, chacun de moyenne $1/\mu$ (absence de mémoire pour
celui en cours) : $E[W] = \frac{E[L] + 1}{\mu} = \frac{1}{\mu - \lambda} = 50$ ms. Formule de Little
$E[L] = \lambda E[W]$. Question bonus.

**29. (N3) Un gestionnaire veut que moins de 10 % des clients trouvent plus de 5 personnes devant eux. Quel $\mu$ faut-il pour $\lambda = 100$ ?**
*Attendu* : $\rho^6 \le 0{,}1 \iff \rho \le 0{,}1^{1/6} \approx 0{,}681 \iff \mu \ge 100/0{,}681 \approx 147$
services par seconde. (Contre 120 aujourd'hui, où c'est un client sur trois.)

**30. (N3) Quelles hypothèses du modèle sont discutables dans la réalité ?**
*Attendu* : services rarement exponentiels (plutôt concentrés autour d'une durée), arrivées pas
toujours poissoniennes (heures de pointe, $\lambda$ variable), clients qui renoncent si la file est
longue, capacité finie. Le modèle M/M/1 donne surtout le bon ordre de grandeur et le message
qualitatif : tout explose quand $\rho \to 1$.

**31. (N1) Quelles coquilles avez-vous relevées dans l'énoncé ?**
*Attendu* : $\rho = \mu/\lambda$ en Q5 (il faut $\lambda/\mu$, sinon probabilités négatives) ; indice de
$I_n$ en B.2 ; « capacité du serveur » pour « de la salle d'attente » ; « cet= algorithme ».

**32. (N2) Que veut dire « test du $\chi^2$ : $p = 0{,}37$ » pour la loi de Poisson simulée ?**
*Attendu* : le test compare les effectifs observés $O_k$ aux effectifs attendus $E_k = T\,P(N = k)$,
via $\sum (O_k - E_k)^2/E_k$. $p$ = probabilité d'un écart au moins aussi grand **si** la loi est
$\mathcal P(4)$. $p = 0{,}37$ : rien d'anormal (on rejetterait si $p < 0{,}01$ ou $0{,}05$). Même idée
pour le test KS (loi continue, plus grand écart entre les fonctions de répartition). *Piège* : dire
« $p = 0{,}37$ donc c'est prouvé » : un test ne prouve pas, il ne détecte pas d'anomalie.
