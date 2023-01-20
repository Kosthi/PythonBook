from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, height):
        super().__init__(first_name, last_name, age, height)
        self.privileges = Privileges()

        
class Privileges():
    def __init__(self):
        self.privileges = ['Can add post', 'Can delete post', 'Can ban user']
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(f"{privilege}")