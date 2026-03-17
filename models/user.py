class User:
    def __init__(self, user_id, name, storage_limit=1000):
        self.user_id = user_id
        self.name = name
        self.storage_limit = storage_limit
        self.used_storage = 0
        self.files = []