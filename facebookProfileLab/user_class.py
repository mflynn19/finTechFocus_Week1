class User:
    def __init__(self, name , email, password, age=13):
        self.name = name
        self.email = email
        self.password = password
        self.age = age
        
    def status_update(self, mood):
        print(self.name+ " is feeling "+mood)
        
    def change_password(self, oldPassword, newPassword):
        pw = input("Enter your old password.\n")
        tries = True
        while tries:
            if pw == oldPassword:
                nPW = input("Enter your new password.\n")
                self.password = newPassword
                tries = False
            else:
                print("Incorrect password. Try again\n")