# Calcule les rendements journaliers du CAC 40 et trace leur histogramme
from pathlib import Path
import matplotlib.pyplot as plt
from data_loader import charger_prix

dossier_figures = Path(__file__).parent.parent / "figures"


def calculer_rendements(prix):
    """Renvoie les rendements journaliers : (prix du jour - prix de la veille) / prix de la veille."""
    rendements = (prix - prix.shift(1)) / prix.shift(1)
    return rendements.dropna()


if __name__ == "__main__":
    prix = charger_prix()
    rendements = calculer_rendements(prix)

    ecart = (rendements - prix.pct_change().dropna()).abs().max()
    print("Écart avec pct_change :", ecart)

    print("Nombre de rendements :", len(rendements))
    print("Rendement moyen (%) :", round(rendements.mean() * 100, 3))
    print("Écart-type (%) :", round(rendements.std() * 100, 3))
    print("Pire jour :", rendements.idxmin().date(), round(rendements.min() * 100, 2), "%")
    print("Meilleur jour :", rendements.idxmax().date(), round(rendements.max() * 100, 2), "%")

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(rendements * 100, bins=100, color="#2a6fdb")
    ax.set_title("CAC 40 : répartition des rendements journaliers (2010-2026)")
    ax.set_xlabel("Rendement journalier (%)")
    ax.set_ylabel("Nombre de jours")
    ax.spines[["top", "right"]].set_visible(False)
    fig.tight_layout()
    fig.savefig(dossier_figures / "histogramme_rendements.png", dpi=150)
    plt.show()