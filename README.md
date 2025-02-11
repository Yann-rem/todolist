# To-Do List en Python avec MongoDB

Ce projet est une application simple de gestion de tâches (To-Do List) en ligne de commande, conçue en Python avec MongoDB comme base de données.

## Fonctionnalités

- **Afficher les tâches** : Liste toutes les tâches présentes dans la base de données.
- **Ajouter une tâche** : Permet d'ajouter une nouvelle tâche avec un statut initial "Nouvelle".
- **Supprimer une tâche** : Supprime une tâche identifiée par son ID.
- **Mettre à jour une tâche** : Modifie la description d'une tâche existante.
- **Mettre à jour le statut d'une tâche** : Change le statut d'une tâche (0 : Nouvelle, 1 : En cours, 2 : Terminée).

## Prérequis

- Python 3.x
- MongoDB en fonctionnement sur `mongodb://localhost:27017/`
- Bibliothèque `pymongo`

## Installation

1. Clonez le projet :

   ```bash
   git clone https://github.com/Yann-rem/todolist.git
   cd todolist
   ```

2. Installez les dépendances :

   ```bash
   pip install pymongo
   ```

3. Assurez-vous que MongoDB est en cours d'exécution.

## Utilisation

1. Lancez l'application :
   ```bash
   python todolist.py
   ```
2. Sélectionnez une option dans le menu principal :
   - **1. Afficher les tâches** : Voir la liste des tâches.
   - **2. Ajouter une tâche** : Ajouter une nouvelle tâche.
   - **3. Supprimer une tâche** : Supprimer une tâche existante en fournissant son ID.
   - **4. Mettre à jour une tâche** : Modifier la description d'une tâche.
   - **5. Mettre à jour le statut d'une tâche** : Changer le statut d'une tâche.
   - **6. Quitter** : Fermer l'application.

## Exemple de Statuts

- **0 : Nouvelle**
- **1 : En cours**
- **2 : Terminée**

## Structure de la Base de Données

Chaque tâche est stockée sous la forme suivante :

```json
{
  "_id": "<identifiant_unique>",
  "description": "<description_de_la_tâche>",
  "status": 0
}
```

## Améliorations possibles

- Gestion des erreurs plus avancée.
- Ajout de la validation des champs.
- Interface utilisateur graphique (GUI).

## Auteur

Ce projet a été conçu pour fournir un exemple simple d'intégration entre Python et MongoDB.
