class File:
    def __init__(self, name, size, owner):
        self.name = name
        self.size = size
        self.owner = owner
        self.versions = ["v1"]