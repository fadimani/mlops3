
# MLOps3 : Prediction des prix immobiliers en Californie

Ce depot GitHub illustre une pipeline **MLOps complete** pour la prediction des prix immobiliers en Californie a partir du jeu de donnees `California Housing`. Le projet couvre l'ensemble du cycle de vie d'un modele de machine learning, y compris la preparation des donnees, l'entrainement, la surveillance en production, et le deploiement, tout en mettant l'accent sur l'automatisation et les bonnes pratiques.

---

## Table des matieres

1. [Contexte et objectifs](#contexte-et-objectifs)
2. [Fonctionnalites](#fonctionnalites)
3. [Technologies utilisees](#technologies-utilisees)
4. [Structure du projet](#structure-du-projet)
5. [Prise en main](#prise-en-main)
6. [Contributeurs](#contributeurs)

---

## Contexte et objectifs

Le but de ce projet est de creer une solution robuste de machine learning pour predire la valeur mediane des maisons en Californie. Il applique les principes **MLOps** pour :

- **Automatiser les pipelines de machine learning**.
- **Assurer une supervision continue** grace a la detection du derive des donnees.
- **Simplifier le reentrainement des modeles** lorsque des changements dans les donnees sont detectes.

---

## Fonctionnalites

1. **Preparation des donnees** :
   - Nettoyage et pretraitement des donnees brutes.
   - Normalisation et division en ensembles d'entrainement/test.

2. **Entrainement des modeles** :
   - Test de plusieurs modeles (regression lineaire, Random Forest, Gradient Boosting).
   - Suivi des experiences avec **MLflow**.
   - Enregistrement du meilleur modele dans le registre de modeles MLflow.

3. **Surveillance en production** :
   - Detection de derive des donnees avec **Evidently**.
   - Generation de rapports HTML pour l'analyse.

4. **Deploiement** :
   - API de prediction avec **FastAPI**.
   - Conteneurisation avec **Docker**.

---

## Technologies utilisees

- **Python** : Langage principal pour la modelisation et les pipelines.
- **MLflow** : Suivi des experiences et gestion des modeles.
- **Evidently** : Surveillance de la derive des donnees.
- **FastAPI** : API pour le deploiement du modele.
- **Docker** : Conteneurisation pour une distribution facile.
- **Pytest** : Tests unitaires.
- **GitHub Actions** : Integration continue (CI/CD).

---

## Structure du Projet MLOps3

mlops3/
├── .github/
│   └── workflows/                         # Configuration des workflows GitHub Actions
├── data/
│   ├── cleaned_california_housing.csv    # Données d'entraînement nettoyées
│   ├── live_data.csv                     # Données simulées en production
├── mlruns/                               # Suivi des expériences avec MLflow
├── reports/
│   ├── data_drift_report.html            # Rapport de dérive des données
├── evidently_monitor.py                  # Surveillance et rapports avec Evidently
├── interface.py                          # Interface utilisateur pour les prédictions
├── main.py                               # Script principal pour l'exécution de la pipeline
├── mission_1.ipynb                       # Notebook pour la mission 1
├── mission_2_&_3.ipynb                   # Notebook pour les missions 2 et 3
├── mission_2_&_3_v2.ipynb                # Version 2 du notebook pour les missions 2 et 3
├── mission_4.py                          # Script pour la mission 4
├── requirements.txt                      # Liste des dépendances Python
├── Dockerfile                            # Fichier Docker pour le déploiement
├── test_mission_4.py                     # Tests unitaires pour la mission 4
└── README.md                             # Documentation du projet


---

## Prise en main

### 1. Cloner le depot
```bash
git clone https://github.com/fadimani/mlops3.git
cd mlops3
```

### 2. Creer un environnement virtuel
```bash
python -m venv venv
source venv/bin/activate  # Linux/MacOS
venv\Scripts\activate   # Windows
```

### 3. Installer les dependances
```bash
pip install -r requirements.txt
```

---

## Contributeurs

- **Fadi Imani** : Createur et mainteneur du projet.
- **Yassir El Hamidi** : Createur et mainteneur du projet.


