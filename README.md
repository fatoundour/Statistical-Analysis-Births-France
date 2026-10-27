# Analyse statistique des naissances en France — Test du χ²

**Projet universitaire · Python · Statistiques inférentielles · Données INSEE (2022)**

## Problématique

> Les naissances en France sont-elles uniformément réparties sur les 365 jours de l'année ?

Ce projet examine la variation du nombre moyen de naissances au cours de l'année 2022 à partir de **moyennes journalières par mois**. Les données disponibles ne sont pas des relevés individuels pour chacun des 365 jours.

## Démarche du projet original

1. Récupération des moyennes journalières mensuelles de naissances.
2. Attribution de la moyenne de chaque mois à chacun de ses jours pour représenter l'évolution sur l'année.
3. Comparaison graphique avec une moyenne annuelle constante.
4. Application d'un test du χ² d'adéquation dans le notebook original.

**Résultats historiques du rapport :** χ² = **572,63**, p-value affichée = **0,00000**, décision rapportée : rejet de H₀ au seuil de 5 %. Ces chiffres décrivent **le calcul du projet original**, et ne constituent pas une validation indépendante du test.

### Limite méthodologique

Les 365 valeurs du graphique sont reconstruites à partir de **12 moyennes mensuelles** : les jours d'un même mois reçoivent la même valeur par construction. La p-value d'un test à 364 degrés de liberté appliqué à ces valeurs reconstruites ne doit donc pas être interprétée comme si l'on disposait de 365 observations journalières indépendantes.

## Vérification complémentaire (ajoutée pour le portfolio)

Le script `scripts/test_mensuel.py` effectue un test du χ² sur **12 effectifs mensuels estimés**, calculés comme `moyenne journalière du mois × nombre de jours du mois`.

- **H₀ :** le taux moyen quotidien de naissances est constant d'un mois à l'autre.
- **H₁ :** ce taux varie selon les mois.
- Les effectifs attendus sont proportionnels au nombre de jours de chaque mois.
- Le test utilise **11 degrés de liberté**.
- Les effectifs sont **approximatifs**, car les moyennes publiées sont arrondies. Ce test ne permet pas de mesurer les variations à l'intérieur d'un mois.

À partir des valeurs conservées : χ² ≈ **572.63** (11 ddl), p-value ≈ **9.99e-116**. Cette analyse complémentaire ne faisait pas partie du rapport initial.

## Organisation

```text
├── data/
│   └── naissances_moyennes_journalieres_2022.csv
├── notebooks/
│   └── analyse_originale_2022.ipynb
├── scripts/
│   └── test_mensuel.py
├── reports/
│   └── rapport_original_test_chi_2.pdf
├── requirements.txt
└── README.md
```

## Exécution

Depuis la racine du dépôt :

```bash
python -m venv .venv
source .venv/bin/activate  # Sur Windows : .venv\Scripts\activate
pip install -r requirements.txt
python scripts/test_mensuel.py
jupyter notebook
```

Ouvrir `notebooks/analyse_originale_2022.ipynb`. **Remarque :** le notebook utilise un chemin `data/...` relatif à la racine du dépôt ; exécutez Jupyter depuis cette racine.

## Source et documentation

- **Source des données :** INSEE, tableau de moyennes journalières mensuelles de naissances, année 2022. Les valeurs de la colonne 2022 ont été conservées dans `data/` ; elles proviennent du tableau fourni avec le projet.
- **Rapport universitaire original :** `reports/rapport_original_test_chi_2.pdf`.

## Technologies

Python, Pandas, NumPy, SciPy, Matplotlib, Jupyter Notebook.
