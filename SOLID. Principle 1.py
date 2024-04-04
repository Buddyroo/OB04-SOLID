class User():
    def __init__(self, user):
        self.user = user

class User_Name_Changer():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.name = new_name

class Save_User():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")



