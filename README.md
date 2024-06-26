# cicdprojet
# Projet de Calculatrice en Python

## Description

Ce projet implémente une simple calculatrice en Python avec les opérations de base : addition, soustraction, multiplication et division. Le projet inclut des tests pour chaque fonction en utilisant `pytest`.

## Structure du Projet

Bien sûr ! Voici un exemple de fichier README.md pour votre projet de calculatrice en Python. Ce fichier explique le but du projet, comment installer les dépendances, comment exécuter le programme principal et comment exécuter les tests.

markdown

# Projet de Calculatrice en Python

## Description

Ce projet implémente une simple calculatrice en Python avec les opérations de base : addition, soustraction, multiplication et division. Le projet inclut des tests pour chaque fonction en utilisant `pytest`.

## Structure du Projet

calculatrice/
│
├── function1.py # Contient les fonctions de la calculatrice
├── main.py # Programme principal pour utiliser la calculatrice
├── test_function1.py # Tests pour les fonctions de la calculatrice
├── README.md # Fichier de documentation (ce fichier)
└── requirements.txt # Liste des dépendances Python

## Prérequis

Assurez-vous d'avoir Python installé sur votre machine. Ce projet a été testé avec Python 3.8+.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone https://github.com/abou94190/cicdprojet.git
   ````powershell
   git clone git@github.com:abou94190/cicdprojet.git
   cd cicdprojet
Installez les dépendances :

bash

    pip install -r requirements.txt

Utilisation

Pour utiliser la calculatrice, exécutez le fichier main.py :

bash

python main.py

Vous verrez un menu vous demandant de choisir une opération (addition, soustraction, multiplication, division) ou de quitter le programme. Entrez les numéros correspondants pour effectuer des calculs.
Tests

Pour exécuter les tests, utilisez pytest. Assurez-vous que pytest est installé :

bash

pip install pytest

Ensuite, exécutez les tests :

bash

pytest test_calculatrice.py

Les résultats des tests seront affichés dans le terminal, indiquant si les tests ont réussi ou échoué.