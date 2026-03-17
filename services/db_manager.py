from pymongo import MongoClient
from models import user
client = MongoClient("mongodb://localhost:27017/")
db = client["cloud_storage"]
collection = db["users"]

class DBManager:

    def add_user(self, user):
        collection.insert_one({
        "id": user.user_id,   
        "name": user.name,
        "storage_limit": user.storage_limit,
        "used_storage": user.used_storage,
        "files": []
    })

    def load_users(self):
        return list(collection.find())

    def update_user(self, user):
        collection.update_one(
            {"id": user.user_id},
            {"$set": {
                "used_storage": user.used_storage,
                "files": [
                    {
                        "name": f.name,
                        "size": f.size,
                        "versions": f.versions
                    } for f in user.files
                ]
            }}
        )