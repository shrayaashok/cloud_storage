from models.user import User
from models.file import File
from services.storage_manager import StorageManager
from services.db_manager import DBManager
from utils.helper import select_user, load_users
db = DBManager()

class CloudSystem:
    def __init__(self):
        self.users = load_users()
        self.storage = StorageManager()

    def create_user(self):
        name = input("Enter name: ")
        user = User(len(self.users) + 1, name)

        self.users.append(user)
        db.add_user(user)

        print("User saved in database!")

    def upload_file(self):
        user = select_user(self.users)
        if not user:
            return

        name = input("File name: ")
        size = int(input("File size: "))

        file = File(name, size, user)
        self.storage.upload_file(user, file)

    def view_files(self):
        user = select_user(self.users)
        if not user:
            return

        for file in user.files:
            print(f"{file.name} | {file.size} | {file.versions}")

    def delete_file(self):
        user = select_user(self.users)
        if not user:
            return

        name = input("File to delete: ")
        self.storage.delete_file(user, name)

    def menu(self):
        while True:
            print("\n---------- Cloud Storage ----------")
            print("1. Create User")
            print("2. Upload File")
            print("3. View Files")
            print("4. Delete File")
            print("5. Exit")

            choice = input("Choice: ")

            if choice == "1":
                self.create_user()
            elif choice == "2":
                self.upload_file()
            elif choice == "3":
                self.view_files()
            elif choice == "4":
                self.delete_file()
            elif choice == "5":
                break
            else:
                print("Invalid!")


if __name__ == "__main__":
    system = CloudSystem()
    system.menu()