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


# Fonction pour ajouter une tâche
def add_task():
    description = input("Entrez la description de la tâche : ")
    task = {"description": description, "status": 0}  # Statut par défaut : Nouvelle
    collection.insert_one(task)
    print("Tâche ajoutée avec succès !")


# Fonction pour supprimer une tâche
def delete_task():
    task_id = input("Entrez l'ID de la tâche à supprimer : ")
    result = collection.delete_one({"_id": task_id})
    if result.deleted_count:
        print("Tâche supprimée avec succès !")
    else:
        print("Aucune tâche trouvée avec cet ID.")
