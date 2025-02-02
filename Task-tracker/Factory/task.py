class Task:
    def __init__(self, name, description, status, id):
        self.name = name
        self.description = description
        self.status = status
        self.id = id

    def getId(self):
        return self.id

    def setStatus(self, status):
        self.status = status
