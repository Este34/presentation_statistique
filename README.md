# TD de statistique — Génération de variables aléatoires

**Le rendu : [`rendu/TD_stats_sujet1_EBP.pdf`](rendu/TD_stats_sujet1_EBP.pdf)**

Sujet 1 : §1.1 inversion de la fonction de répartition (loi exponentielle) · §1.2 méthode de
Box-Muller (gaussiennes). Python (numpy, matplotlib), graine 2026, T = 10 000 tirages.

## Contenu

```
rendu/TD_stats_sujet1_EBP.pdf   le TD en PDF
sujets/sujet1/
  enonce.md                     énoncé transcrit
  demonstrations.md             démonstrations complètes
  s1_1_inversion.ipynb          §1.1 — code, figures, commentaires
  s1_2_box_muller.ipynb         §1.2 — code, figures, commentaires
  TD_stats_sujet1_colab.ipynb   §1.1 + §1.2 en un notebook autonome (Google Colab / Kaggle)
  matlab_python.md              fonctions Matlab de l'énoncé → équivalents Python
  figures/                      figures et chiffres clés (resultats.json)
src/stats_td/                   générateurs (inversion, Box-Muller) et fonctions de répartition empiriques
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
