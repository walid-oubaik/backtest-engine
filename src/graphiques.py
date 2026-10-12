# Trace l'évolution du prix de clôture du CAC 40 et enregistre le graphique dans figures/
from pathlib import Path
import matplotlib.pyplot as plt
from data_loader import charger_prix

dossier_figures = Path(__file__).parent.parent / "figures"


def tracer_prix(prix):
    """Trace le prix de clôture et enregistre l'image dans figures/prix_cac40.png."""
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(prix.index, prix, color="#2a6fdb", linewidth=1.5)
    ax.set_title("CAC 40 : prix de clôture quotidien (2010-2026)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Points")
    ax.grid(alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(dossier_figures / "prix_cac40.png", dpi=150)
    plt.show()


if __name__ == "__main__":
    prix = charger_prix()
    tracer_prix(prix)
    