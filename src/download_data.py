# Télécharge les prix quotidiens du CAC 40 depuis Yahoo Finance et les enregistre dans data/cac40.csv
from pathlib import Path
import yfinance as yf

# Paramètres du téléchargement
symbole = "^FCHI"
date_debut = "2010-01-01"
date_fin = "2026-10-01"

# Emplacement du fichier de sortie : le dossier data/ du projet
dossier_projet = Path(__file__).parent.parent
chemin_fichier = dossier_projet / "data" / "cac40.csv"

# Téléchargement des prix
donnees = yf.download(symbole, start=date_debut, end=date_fin, multi_level_index=False)

# Enregistrement dans le fichier CSV
donnees.to_csv(chemin_fichier)

print("Nombre de jours téléchargés :", len(donnees))

