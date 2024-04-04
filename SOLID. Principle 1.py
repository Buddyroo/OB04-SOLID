class User():
    def __init__(self, user):
        self.user = user

class User_Name_Changer():
    def __init__(self, user):
        self.user = user

    def change_name(self, new_name):
        self.user.user = new_name

class Save_User():
    def __init__(self, user):
        self.user = user

    def save(self):
        file = open("users.txt", "a")
        file.write(f"{self.user.user}\n")
        file.close()


user=User("Anna")

save = Save_User(user)
save.save()

name_changer=User_Name_Changer(user)
name_changer.change_name("Daniel")

save = Save_User(user)
save.save()

print(user.user)


