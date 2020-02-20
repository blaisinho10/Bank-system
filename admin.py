from person import person

class Admin(person):
    def __init__(self,fname, lname, address, user_name, password, full_rights):
        super().__init__(fname, lname, address)
        self.user_name = user_name
        self.password = password
        self.full_admin_rights = full_rights
         
    
    def set_username(self, uname):
        self.user_name = uname
        
    def get_username(self):
        return self.user_name
    
    def set_password(self, password):
        self.password = password
    
    def get_password(self):
        return self.password
    
    def set_full_admin_right(self, admin_right):
        self.full_admin_rights = admin_right

    def has_full_admin_right(self):
        return self.full_admin_rights

