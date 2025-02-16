from pymongo import MongoClient

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["todolist"]
collection = db["tasks"]

# Statuts des tâches
status_labels = {0: "Nouvelle", 1: "En cours", 2: "Terminée"}
