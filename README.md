# TD de statistique

**Les rendus : [`rendu/TD_stats_sujet1_EBP.pdf`](rendu/TD_stats_sujet1_EBP.pdf) (sujet 1) · [`rendu/TD_stats_sujet3_EBP.pdf`](rendu/TD_stats_sujet3_EBP.pdf) (sujet 3)**

Sujet 1 : §1.1 inversion de la fonction de répartition (loi exponentielle) · §1.2 méthode de
Box-Muller (gaussiennes). Python (numpy, matplotlib), graine 2026, T = 10 000 tirages.

Sujet 3 : optimisation de h(x) = x² + 3x cos x sur [-8π, 8π], gradient simple contre recuit simulé
(1000 itérations, 1000 lancers du recuit pour estimer son taux de succès).

## Contenu

```
rendu/TD_stats_sujet1_EBP.pdf   le TD 1 en PDF
rendu/TD_stats_sujet3_EBP.pdf   le TD 3 en PDF (source : rendu/sources/sujet3.tex, xelatex)
sujets/sujet1/
  enonce.md                     énoncé transcrit
  demonstrations.md             démonstrations complètes
  s1_1_inversion.ipynb          §1.1 — code, figures, commentaires
  s1_2_box_muller.ipynb         §1.2 — code, figures, commentaires
  TD_stats_sujet1_colab.ipynb   §1.1 + §1.2 en un notebook autonome (Google Colab / Kaggle)
  matlab_python.md              fonctions Matlab de l'énoncé → équivalents Python
  figures/                      figures et chiffres clés (resultats.json)
sujets/sujet3/
  enonce.md, demonstrations.md  énoncé transcrit (coquilles signalées), démonstrations
  s3_1_recuit_simule.ipynb      Q1-Q4 : code, figures, commentaires chiffrés
  s3_1_explique.ipynb           le même sujet expliqué depuis zéro (exercices, réponses orales)
  questions_oral.md, fiche_revision.md, matlab_python.md
  matlab/                       le même TD en Matlab (s3_recuit_simule.m + recuit.m, testé sous Octave 8.4)
                                et son équivalent Python ligne à ligne (s3_recuit_simule.py)
src/stats_td/                   générateurs (inversion, Box-Muller), répartitions empiriques, optimisation (gradient, recuit)
tests/                          tests statistiques (moyennes, variances, Kolmogorov-Smirnov, pente)
```

## Relancer le code

```bash
pip install -r requirements.txt
python -m pytest
jupyter notebook sujets/sujet1/
```

Sans installation : importer `sujets/sujet1/TD_stats_sujet1_colab.ipynb` dans Google Colab
(*Fichier → Importer un notebook*), puis *Tout exécuter*.
