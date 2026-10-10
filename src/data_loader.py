# Charge les prix de clôture du CAC 40 depuis data/cac40.csv et vérifie leur qualité
from pathlib import Path
import pandas as pd

chemin_donnees = Path(__file__).parent.parent / "data" / "cac40.csv"


def charger_prix(chemin=chemin_donnees):
    """Renvoie les prix de clôture du CAC 40, indexés par date."""
    donnees = pd.read_csv(chemin, index_col="Date", parse_dates=True)
    prix = donnees["Close"]
    return prix


if __name__ == "__main__":
    prix = charger_prix()
    print("Nombre de jours :", len(prix))
    print("Première date :", prix.index[0])
    print("Dernière date :", prix.index[-1])
    print("Valeurs manquantes :", prix.isna().sum())
    print("Dates dans l'ordre :", prix.index.is_monotonic_increasing)