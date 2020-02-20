class person(object):
    def __init__(self, fname, lname, address,):
        self.fname = fname
        self.lname = lname
        self.address = address
        
    def update_address(self, number,street,town,post_code):
         self.address["n"] = number
         self.address["street"] = street
         self.address["town"] = town
         self.address["post_code"] = post_code
    
    def get_address(self):
        return self.address 
    
    def get_address_no(self):
        return self.address["n"]
    
    def get_address_street(self):
        return self.address["street"]
    
    def get_address_town(self):
        return self.address["town"]
    
    def get_address_post_code(self):
        return self.address["post_code"]
    
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
