# Sujet 4 · Étude de la file M/M/1

> Transcription de l'énoncé papier (pages 23-26). Les fonctions Matlab utiles sont traduites
> en Python dans [matlab_python.md](matlab_python.md). Les coquilles sont signalées dans des
> encadrés ⚠️, sans toucher au texte de l'énoncé.

Les situations de la vie courante dans lesquelles on est confronté à un phénomène d'attente sont
innombrables : file d'attente de clients devant un guichet unique, clients arrivant aux m caisses
d'un supermarché, avions tournant au-dessus d'un aéroport en attendant qu'une piste se libère,
machines tombant en panne et attendant qu'un réparateur soit libre, appels téléphoniques en
attente qu'une ligne se libère, tâches se partageant les ressources d'un seul ou de plusieurs
processeurs...

La file M/M/1 est le modèle de file d'attente le plus simple à étudier. Ce STP porte sur l'étude
de la file notée M/M/1 dans la notation de Kendall :
- M : les clients arrivent selon un processus de Poisson ;
- M : les temps de service de chacun des clients sont indépendants et identiquement distribués
  suivant une loi exponentielle ;
- 1 : il y a un seul serveur.

La discipline de service est du type FIFO (First In First Out) ce qui signifie que les clients
sont servis dans leur ordre d'arrivée. La capacité du serveur est infinie c'est-à-dire que la
longueur de la file d'attente n'est pas limitée supérieurement.

> ⚠️ **Formulation** : c'est la capacité de la **salle d'attente** qui est infinie (aucun client
> n'est refusé), pas celle du serveur, qui traite un client à la fois. Dans tout le sujet, la
> « longueur de la file » $L$ compte **tous** les clients présents : ceux qui attendent **et**
> celui qui est servi. C'est avec cette convention que $P(L = k) = (1-\rho)\rho^k$ est juste.

## Préliminaire : quelques notions sur le processus de Poisson

**A. La loi exponentielle** de paramètre $\lambda$ est la loi de fonction de répartition
complémentaire
```math
F^c(x) = P(X \ge x) = \mathbb 1_{\mathbb R^+}(x)\exp(-\lambda x) + \mathbb 1_{\mathbb R^{*-}}(x).
```

1. Montrer que la loi exponentielle a même moyenne et même écart-type et donner l'expression de
   sa moyenne et de son écart type en fonction de $\lambda$.
2. Montrer que la loi exponentielle est « sans mémoire » c'est-à-dire que
   ```math
   (*) \qquad P(X \ge x + t \mid X \ge x) = P(X \ge t)
   ```
   ce qui signifie que si cette variable aléatoire représente un temps de vie la durée de vie
   résiduelle est indépendante du temps de vie déjà écoulé.
3. Montrer que la loi exponentielle est la seule loi sans mémoire c'est-à-dire la seule loi
   vérifiant $(*)$.

   > ⚠️ **Précision** : « la seule » parmi les lois **à densité** sur $\mathbb R^+$ (ou plus
   > généralement les lois sur $\mathbb R^+$ avec $0 < P(X \ge x) $ pour tout $x$). La relation
   > $(*)$ doit être lue pour tous $x, t \ge 0$. Les cas dégénérés $P(X \ge x) = 0$ (où la
   > probabilité conditionnelle n'a pas de sens) et la masse en 0 sont exclus ; en discret, la
   > loi géométrique est elle aussi sans mémoire. Voir [demonstrations.md](demonstrations.md#a3).

La loi exponentielle est très souvent utilisée pour modéliser des durées (durée de vie d'une
ampoule, temps de service d'un client, durée d'exécution d'une tâche sur une chaîne de
production...).

**B. Un processus ponctuel** est un processus représentant la répartition de points sur un
ensemble (par exemple la droite réelle), ces points ne pouvant pas être agrégés par paquets. Les
processus ponctuels sont souvent utilisés pour représenter les instants d'arrivée d'événements
(arrivées de clients à un guichet, instants de panne d'une machine, instants de désintégration de
particules...).

Le processus de Poisson est un processus ponctuel tel que les durées séparant deux événements
sont indépendantes et identiquement distribuées suivant une loi exponentielle $\mathcal E(\lambda)$
où le paramètre $\lambda$ est l'intensité du processus (nombre moyen d'événements par unité de
temps).

1. Soit $X_1$ et $X_2$ deux variables aléatoires à densité et indépendantes. On note $f(x)$ et
   $g(x)$ les densités de $X_1$ et $X_2$. Montrer que $Z = X_1 + X_2$ a pour densité $f * g(x)$
   en notant $f * g$ le produit de convolution de $f$ et de $g$.
2. Notons $I_n$ le temps séparant la survenue du $n$-ième et du $(n+1)$-ième événement dans un
   processus de Poisson d'intensité $\lambda$. Notons $T_n = \sum_{k=1}^n I_k$ l'instant auquel
   survient le $n$-ième événement. $I_1 \sim \mathcal E(\lambda)$. Montrer que $T_2$ est
   distribuée suivant une loi d'Erlang de densité $f_2(x) = \lambda^2 x \exp(-\lambda x)$.
   Montrer par récurrence que $T_k$ est distribuée suivant une loi d'Erlang de densité
   ```math
   f_k(x) = \frac{\lambda^k x^{k-1}}{(k-1)!}\exp(-\lambda x).
   ```

   > ⚠️ **Coquille d'indice** : avec $T_n = \sum_{k=1}^n I_k$ instant du $n$-ième événement,
   > $I_n$ sépare le $(n-1)$-ième et le $n$-ième événement, en comptant l'origine $t = 0$ comme
   > « événement 0 » ($T_0 = 0$, $I_1 = T_1$). Avec la phrase de l'énoncé, $T_n$ serait l'instant
   > du $(n+1)$-ième. Les densités $f_k$ sont valables pour $x \ge 0$ (elles valent 0 pour $x < 0$).

3. On note $N_t$ le nombre d'événements survenant sur l'intervalle $[0, t]$. Déduire de la
   question précédente que $N_t$ est distribuée suivant une loi de Poisson de paramètre
   $\lambda t$
   ```math
   P(N_t = k) = \exp(-\lambda t)\frac{(\lambda t)^k}{k!}.
   ```
   Indication : remarquer que $\{N_t = k\} = \{T_k \le t < T_{k+1}\}$.

## Simulation d'une variable aléatoire distribuée suivant une loi de Poisson

1. Simulation d'une variable aléatoire $\mathcal E(\lambda)$. Montrer que si
   $U \sim \mathcal U[0,1]$ alors $X = -\frac{1}{\lambda}\log U$ est $\mathcal E(\lambda)$.

   > ⚠️ **Détail** : $\log U$ n'est pas défini si $U = 0$ (possible avec `rand` : valeurs dans
   > $[0, 1[$). On utilise $1 - U$, qui suit aussi $\mathcal U[0,1]$ et vaut dans $]0, 1]$
   > (comme au sujet 1). $\log$ désigne le logarithme **népérien** (`log` en Matlab).

2. Soit $N \sim \mathcal P(\lambda)$. Si $(X_i)_i$ sont des variables aléatoires indépendantes et
   de même distribution $\mathcal E(\lambda)$ on a
   ```math
   N = \sum_{i=1}^{\infty} \mathbb 1_{Z_i \le 1}
   ```
   avec $Z_i = \sum_{1 \le j \le i} X_j$.
   En déduire un algorithme permettant de simuler une variable $\mathcal P(\lambda)$.

   > ⚠️ **Lecture** : c'est une égalité **en loi** : la somme a la loi $\mathcal P(\lambda)$
   > (c'est $N_1$ de la question B.3, avec $t = 1$). Les $Z_i$ sont les instants d'un processus
   > de Poisson d'intensité $\lambda$, et la somme compte ceux qui tombent dans $[0, 1]$.

## Étude par simulation de la file M/M/1

Les instants d'arrivée de clients dans la file d'attente sont distribués suivant un processus de
Poisson d'intensité $\lambda$. Les temps de service de chacun des clients sont indépendants et
identiquement distribués suivant une loi exponentielle $\mathcal E(\mu)$.

Nous supposons qu'à l'instant $t = 0$ la file est vide. Nous allons étudier l'évolution de la
longueur de la file d'attente aux instants successifs où un nouveau client se présente ou plutôt
juste avant qu'un nouveau client ne se présente.

Notons $N(t)$ le processus de Poisson d'intensité $\mu$. Notons $L(t)$ la longueur de la file
d'attente à l'instant $t$ et $L_n = L(T_n^-)$ la longueur de la file juste avant que ne se
présente le $n$-ième client.

> ⚠️ **Précision** : $N(t)$ est un processus de Poisson d'intensité $\mu$ **indépendant** des
> arrivées ; ses points sont les instants où un service se terminerait si le serveur travaillait
> sans arrêt (« services potentiels »). Cela marche grâce à l'absence de mémoire de
> $\mathcal E(\mu)$. $T_n$ désigne ici l'instant d'arrivée du $n$-ième client, et $L_1 = 0$ (file
> vide au départ).

1. Montrer que l'évolution de la longueur de la file d'attente juste avant arrivée de client est
   régie par
   ```math
   L_{n+1} = (L_n + 1 - A_n)^+ = \max(0, L_n + 1 - A_n)
   ```
   où $A_n = N(T_{n+1}) - N(T_n)$ est distribuée comme le nombre de clients qui seraient servis
   dans l'intervalle $[T_n, T_{n+1}[$ si la file ne se vidait pas dans l'intervalle.
2. En déduire un algorithme de simulation de l'évolution de la longueur de la file d'attente.
   Implémenter cet~~=~~ algorithme.

   > ⚠️ **Coquille** : « cet= algorithme », lire « cet algorithme ».

**Influence du paramètre de charge.** On note $\rho = \frac{\lambda}{\mu}$ la charge de la file
d'attente ($= \frac{\text{TempsDeServiceMoyen}}{\text{TempsMoyenEntre2Arrivées}}$). Nous allons
montrer expérimentalement que ce paramètre a une influence capitale sur le type de comportement de
la file d'attente.

3. $\rho > 1$ : choisir deux valeurs de $\lambda$ et $\mu$ telles que $\rho > 1$ et montrer par
   simulation que la file croît alors indéfiniment.
4. $\rho < 1$ : choisir deux valeurs de $\lambda$ et $\mu$ telles que $\rho < 1$ et montrer par
   simulation que le comportement de la file se stationnarise.
5. Choisir les valeurs suivantes pour les paramètres $\lambda$ et $\mu$ : $\lambda = 100$
   arrivées par seconde en moyenne, $\mu = 120$ départs par seconde en moyenne dans les
   situations où le serveur est en permanence occupé. Simuler l'évolution de la file d'attente
   sur une durée de 5 minutes.
   Vérifier par simulation que la distribution de la longueur de la file d'attente est
   $P(L_n = k) = (1 - \rho)\rho^k$ où $\rho = \frac{\mu}{\lambda}$.

   > ⚠️ **Coquille** : il faut $\rho = \frac{\lambda}{\mu}$ (définition donnée juste au-dessus).
   > Avec $\frac{\mu}{\lambda} = 1{,}2$, $(1-\rho)\rho^k$ serait **négatif** : ce ne serait pas
   > une loi de probabilité. Ici $\rho = \frac{100}{120} = \frac{5}{6} \approx 0{,}833$. La formule
   > décrit la loi **limite** (régime stationnaire), atteinte en pratique au bout de quelques
   > secondes.

   En déduire l'expression analytique (en fonction de $\rho$) :
   - de la moyenne et de la variance de la longueur de la file ;
   - de la probabilité qu'un client qui arrive trouve le serveur libre ;
   - de la probabilité qu'un client qui arrive trouve plus de 5 clients avant lui

   et vérifier que les valeurs obtenues par simulation sont cohérentes avec ces ordres de grandeur.

   > ⚠️ **Interprétation** : « plus de 5 clients » est lu au sens strict, $L > 5$, soit
   > $L \ge 6$ : $P = \rho^6$. Au sens large ($L \ge 5$) on aurait $\rho^5$.

**Fonctions Matlab utiles** (non listées dans cette partie de l'énoncé, mêmes que les sujets
précédents) : `rand`, `log`, boucles `for` / `while`, `max`, `cumsum`, `mean`, `var`, `hist`,
`plot`, `stairs`, `bar`, `semilogy`.
