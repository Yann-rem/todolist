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


# Fonction pour mettre à jour la description d'une tâche
def update_task():
    task_id = input("Entrez l'ID de la tâche à mettre à jour : ")
    new_description = input("Entrez la nouvelle description : ")
    result = collection.update_one(
        {"_id": task_id}, {"$set": {"description": new_description}}
    )
    if result.matched_count:
        print("Description mise à jour avec succès !")
    else:
        print("Aucune tâche trouvée avec cet ID.")


# Fonction pour mettre à jour le statut d'une tâche
def update_task_status():
    task_id = input("Entrez l'ID de la tâche à mettre à jour : ")
    print("Statuts disponibles :")
    for key, value in status_labels.items():
        print(f"{key}: {value}")
    new_status = int(input("Entrez le nouveau statut (0, 1 ou 2) : "))
    if new_status not in status_labels:
        print("Statut invalide.")
        return
    result = collection.update_one({"_id": task_id}, {"$set": {"status": new_status}})
    if result.matched_count:
        print("Statut mis à jour avec succès !")
    else:
        print("Aucune tâche trouvée avec cet ID.")


# Menu principal
def main():
    while True:
        print("\n--- Menu To-Do List ---")
        print("1. Afficher les tâches")
        print("2. Ajouter une tâche")
        print("3. Supprimer une tâche")
        print("4. Mettre à jour une tâche")
        print("5. Mettre à jour le statut d'une tâche")
        print("6. Quitter")

        choice = input("Choisissez une option : ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            update_task()
        elif choice == "5":
            update_task_status()
        elif choice == "6":
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if __name__ == "__main__":
    main()
