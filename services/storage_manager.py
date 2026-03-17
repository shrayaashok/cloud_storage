from services.db_manager import DBManager
db = DBManager()

class StorageManager:

    def upload_file(self, user, file):
        if user.used_storage + file.size > user.storage_limit:
            print("Storage limit exceeded!")
            return

        user.files.append(file)
        user.used_storage += file.size

        db.update_user(user)

        print("File uploaded and saved to database!")

    def delete_file(self, user, file_name):
        for file in user.files:
            if file.name == file_name:
                user.files.remove(file)
                user.used_storage -= file.size

                db.update_user(user)

                print("File deleted!")
                return

        print("File not found!")