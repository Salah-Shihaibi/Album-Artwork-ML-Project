class User():
    def __init__(self, username:str, name:str, password:str, email:str):
        self.username = username
        self.name = name
        self.password = password
        self.email = email
    def self_dict( self ):
         return {
                   'username' : self.username,
                   'name'  : self.name, 
                   'password' : self.password,
                   'email' : self.email
                }
    
