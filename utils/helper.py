from models.user import User
from models.file import File
from services.db_manager import DBManager
db = DBManager()

def load_users():
    data = db.load_users()
    users = []

    for u in data:
        user = User(u["id"], u["name"], u["storage_limit"])
        user.used_storage = u["used_storage"]

        for f in u.get("files", []):
            file = File(f["name"], f["size"], user)
            file.versions = f["versions"]
            user.files.append(file)

        users.append(user)

    return users


def select_user(users):
    if not users:
        print("No users found!")
        return None

    for i, user in enumerate(users):
        print(f"{i}: {user.name}")

    idx = int(input("Select user index: "))
    return users[idx]