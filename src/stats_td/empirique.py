"""Estimateurs empiriques : fonction de répartition et pente en semi-log."""

import numpy as np


def repartition_histogramme(echantillon, bins=100):
    """F estimée à partir de l'histogramme (méthode de l'énoncé : hist + cumsum).

    Renvoie (bords droits des classes, F aux bords droits).
    """
    effectifs, bords = np.histogram(echantillon, bins=bins)
    F = np.cumsum(effectifs) / len(echantillon)
    return bords[1:], F


def repartition_empirique(echantillon):
    """F_n(y) = (1/n) #{i : Y_i <= y}, évaluée aux points triés."""
    y = np.sort(echantillon)
    F = np.arange(1, len(y) + 1) / len(y)
    return y, F


def repartition_complementaire(echantillon):
    """F^c_n(y) = P_n(Y >= y) = (1/n) #{i : Y_i >= y}, aux points triés.

    Toujours > 0 aux points de l'échantillon (au moins le point lui-même),
    donc le log est défini : pratique pour l'échelle semi-log.
    """
    y = np.sort(echantillon)
    n = len(y)
    Fc = (n - np.arange(n)) / n
    return y, Fc


def pente_semilog(echantillon, quantile_max=0.99):
    """Pente de ln F^c_n(y) en fonction de y (régression linéaire).

    Remplace ``ginput`` : au lieu de cliquer deux points, on ajuste une
    droite sur la partie bien peuplée (on écarte la queue, trop bruitée
    car il y reste très peu de points). Pour E(lam), la pente vaut -lam.
    """
    y, Fc = repartition_complementaire(echantillon)
    garde = y <= np.quantile(echantillon, quantile_max)
    pente, ordonnee = np.polyfit(y[garde], np.log(Fc[garde]), 1)
    return pente, ordonnee
