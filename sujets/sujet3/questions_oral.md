# Sujet 3 — Questions probables du jury

Niveaux : **N1** définition / restitution · **N2** démonstration / calcul · **N3** « et si… », recul.
Chiffres : notebook `s3_1_recuit_simule.ipynb` (graine 2026), voir [fiche_revision.md](fiche_revision.md).

---

**1. (N1) Quelle est la différence entre un minimum local et un minimum global ?**
*Attendu* : local = plus petit que les points voisins ; global = plus petit que tous les points
de l'intervalle. Ici 9 minima locaux, un seul global ($x^\star \approx -0{,}637$, $h \approx -1{,}130$).
*Piège* : dire que le gradient « trouve le minimum » sans préciser lequel.

**2. (N1) Écrivez l'itération du gradient simple et expliquez chaque terme.**
*Attendu* : $x_{n+1} = x_n - \alpha_n h'(x_n)$ ; $-h'$ donne la direction de descente, $\alpha_n$
la longueur du pas. *Piège* : signe + (on monterait).

**3. (N2) Calculez $h'(x)$.**
*Attendu* : $h'(x) = 2x + 3\cos x - 3x\sin x$, dérivée d'un produit pour $3x\cos x$.
*Piège* : oublier le terme $3\cos x$.

**4. (N2) Pourquoi $h$ diminue-t-elle à chaque pas du gradient ?**
*Attendu* : Taylor, $h(x_n - \alpha h') \approx h(x_n) - \alpha\,h'(x_n)^2 \le h(x_n)$, valable pour un
pas assez petit. Vérifié : $h$ décroît à chaque pas dans le notebook.

**5. (N2) À quoi servent les conditions $\sum \alpha_n = +\infty$ et $\sum \alpha_n^2 < \infty$ ? Vérifiez-les pour $\alpha_n = 0{,}025/n$.**
*Attendu* : la 1re évite de s'arrêter trop tôt (déplacement total borné sinon) ; la 2e fait
tendre les pas vers 0 pour ne pas osciller. $\sum 1/n$ diverge (harmonique), $\sum 1/n^2 = \pi^2/6$.
*Piège* : confondre les deux rôles.

**6. (N2) Pourquoi le gradient parti de 7,5 ne trouve-t-il pas le minimum global ?**
*Attendu* : 7,5 est dans le bassin de 8,814 (entre les maxima 7,14 et 13,37) ; $h'(7{,}5) < 0$,
donc on va à droite ; pour rejoindre le global il faudrait **remonter** le col en 7,14, ce que
le gradient ne fait jamais.

**7. (N2) Le gradient a-t-il convergé après 1000 itérations ?**
*Attendu* : vers le bon minimum local oui en tendance, mais pas en précision : $x_{1000} = 8{,}661$
contre $8{,}814$ (écart 0,153). Erreur en $n^{-c}$, $c = 0{,}025\,h''(\bar x) \approx 0{,}505$ :
pente log-log mesurée $-0{,}494$. *Piège* : dire « il a convergé » sans chiffre.

**8. (N3) D'où vient la vitesse $n^{-c}$ ? Comment l'accélérer ?**
*Attendu* : $e_{n+1} \approx (1 - c/n)\,e_n$, produit $\approx n^{-c}$ (car $\sum 1/k \approx \ln n$).
Pas constant $\alpha < 2/h''$ : convergence géométrique $(1 - \alpha h'')^n$. Ou Newton
($\alpha = 1/h''$).

**9. (N1) Décrivez une itération du recuit simulé.**
*Attendu* : tirer $z \sim \mathcal U[x_n - \pi/2, x_n + \pi/2]$ ; si $h(z) \le h(x_n)$ on accepte ; sinon
on accepte avec probabilité $e^{-\Delta h/T_n}$ ; sinon on reste.

**10. (N2) Comment accepte-t-on « avec probabilité $p$ » en pratique ?**
*Attendu* : $U \sim \mathcal U[0,1]$, accepter si $U < p$, car $P(U < p) = F_U(p) = p$. Lien avec
le sujet 1 (fonction de répartition de l'uniforme). *Piège* : comparer $p$ à 0,5.

**11. (N2) Rôle de la température : que se passe-t-il si $T$ est très grand ? très petit ?**
*Attendu* : $T$ grand : $e^{-\Delta/T} \approx 1$, presque tout accepté, marche aléatoire qui explore
(taux 0,99 au début) ; $T \to 0$ : on n'accepte plus que les descentes (taux 0,09 à la fin).

**12. (N3) Pourquoi le recuit vise-t-il le minimum global et pas un minimum local ?**
*Attendu* : à $T$ fixé, équilibre détaillé avec proposition symétrique, loi stationnaire
$\mu_T \propto e^{-h/T}$ (Boltzmann) ; $\mu_T(x)/\mu_T(x^\star) = e^{-(h(x) - h(x^\star))/T} \to 0$ : concentration sur
les minima globaux quand $T \to 0$.
*Piège* : « parce qu'il est aléatoire » (insuffisant).

**13. (N3) L'énoncé dit que ce choix de $T_n$ garantit la convergence presque sûre. Qu'en pensez-vous ?**
*Attendu* : c'est faux. Avec $T_n = T_0\alpha^n$, $\sum e^{-d/T_n} < \infty$ : par Borel-Cantelli la
chaîne ne franchit plus qu'un nombre fini de cols, elle gèle. Hajek (espace fini) donne une
convergence **en probabilité** avec $T_n = c/\ln n$, $c \ge d^\star$ (profondeur du minimum local non
global le plus profond : $\approx 26$ à petits pas, $\approx 12$ avec des sauts $\pm\pi/2$). Observé :
73,8 % ± 2,7 % de succès sur 1000 lancers, 25,9 % piégés en 2,805.
*Piège* : dire « presque sûre » pour Hajek.

**14. (N3) Pourquoi justement le piège en 2,805, et pourquoi environ 25 % ?**
*Attendu* : c'est le minimum local le plus bas ($h = -0{,}075$, à 1,06 du global), derrière un
col bas (2,75). Quand $T$ passe sous $\approx 1$ ($n \approx 618$), la chaîne ne franchit plus le col :
elle « gèle ». À $T = 1$, la loi de Boltzmann met $\approx 25$ % de sa masse dans ce bassin.

**15. (N3) Refroidir plus lentement règle-t-il le problème ?**
*Attendu* : $\alpha = 0{,}995$, $N = 2000$ : 77,0 % ± 4,1 % contre 73,8 % : écart de 1,27 erreur-type,
non significatif. Il faudrait un refroidissement logarithmique (trop lent) ou plusieurs lancers.

**16. (N2) Comment avez-vous évalué le recuit, puisqu'il est aléatoire ?**
*Attendu* : 1000 lancers indépendants, proportion de succès $\hat p$, erreur-type
$\sqrt{\hat p(1-\hat p)/R} \approx 0{,}014$, IC à 95 % $\hat p \pm 1{,}96 \times$ erreur-type. *Piège* : conclure
sur un seul lancer.

**17. (N3) Comment combiner les deux méthodes ?**
*Attendu* : recuit pour trouver le bon bassin, puis gradient depuis le meilleur point pour
affiner ; ou plusieurs recuits (2 lancers : échec $0{,}262^2 \approx 7$ %) ; ou gradient *multistart*.

**18. (N1) Pourquoi ne pas simplement prendre le `min` de la grille de 5000 points ?**
*Attendu* : en 1D ça marche (trouve $-0{,}6385$ à 0,01 près), mais en dimension $d$ il faudrait
$5000^d$ points. La 1D sert à visualiser.

**19. (N2) Pourquoi le minimum global est-il forcément dans $]-3, 3[$ ?**
*Attendu* : $3x\cos x \ge -3|x|$ donc $h(x) \ge |x|(|x|-3) > 0$ pour $|x| > 3$, alors que
$h(-0{,}637) < 0$.

**20. (N3) Avez-vous repéré des coquilles dans l'énoncé ?**
*Attendu* : « $h = -h$ » (lire $\tilde h = -h$) ; $(n-1)/5000$ n'atteint pas $8\pi$ (diviser par 4999,
`linspace`) ; $\alpha$ utilisé pour deux choses ; $\alpha_n = O(1/n)$ ne suffit pas pour
$\sum\alpha_n = \infty$ ; $\alpha_0 = 0{,}025/0$ non défini ; « extrema globaux » pour « minima
globaux » ; « garantit la convergence p.s. » faux.

**21. (N3, bonus hors programme strict) Quel lien avec l'algorithme de Metropolis–Hastings ?**
*Attendu* : la règle d'acceptation est celle de Metropolis pour la loi $\mu_T$ ; le recuit est un
Metropolis dont on fait baisser la température.
