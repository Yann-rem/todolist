from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todolist"]
collection = db["tasks"]

# Statuts des tâches
status_labels = {0: "Nouvelle", 1: "En cours", 2: "Terminée"}


# Fonction pour afficher les tâches
def show_tasks():
    tasks = list(collection.find())
    if not tasks:
        print("\nAucune tâche disponible.\n")
    else:
        print("\nListe des tâches :")
        for task in tasks:
            print(
                f"ID: {task['_id']} | Description: {task['description']} | Statut: {status_labels[task['status']]}"
            )
