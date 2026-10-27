"""Vérification complémentaire : test d'un taux quotidien constant entre les mois de 2022.
Les effectifs mensuels sont estimés à partir des moyennes journalières publiées,
qui sont arrondies. Résultats donc approximatifs.
"""
import csv
from pathlib import Path
from scipy.stats import chisquare

source = Path(__file__).resolve().parents[1] / "data" / "naissances_moyennes_journalieres_2022.csv"
with source.open(encoding="utf-8", newline="") as f:
    lignes = list(csv.DictReader(f))
jours = [int(ligne["jours_dans_le_mois"]) for ligne in lignes]
moyennes = [float(ligne["moyenne_journaliere_2022"]) for ligne in lignes]
observes = [j * m for j, m in zip(jours, moyennes)]  # Effectifs mensuels estimés
attendus = [sum(observes) * j / sum(jours) for j in jours]
statistique, p_value = chisquare(observes, attendus)
print(f"Chi-deux (12 mois, 11 ddl) : {statistique:.2f}")
print(f"p-value : {p_value:.3e}")
print("H0 : taux moyen quotidien constant d'un mois à l'autre.")
print("Attention : effectifs mensuels estimés à partir de moyennes arrondies.")
