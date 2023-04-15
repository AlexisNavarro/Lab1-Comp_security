#users

#sets the account names and passwords
class accounts:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    #get the username     
    def getUsername(self):
        return self.username

    #get the password
    def getPassword(self):
        return self.password
    
    