"""Style commun des figures (notebooks et présentations)."""

from pathlib import Path

import matplotlib.pyplot as plt

BLEU = "#2a6fdb"
ORANGE = "#e8743b"


def style():
    plt.rcParams.update(
        {
            "figure.figsize": (7, 4.2),
            "figure.dpi": 110,
            "axes.grid": True,
            "grid.alpha": 0.3,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "font.size": 11,
        }
    )


def sauver(fig, chemin):
    chemin = Path(chemin)
    chemin.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(chemin, dpi=150, bbox_inches="tight")
