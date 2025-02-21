class User:
    def __init__(self, id: int, username: str):
        self.id = id
        self.username = username
        self.followers = 0

    def add_subscriber(self):
        self.followers += 1



user_1 = User(1, "pesho")


