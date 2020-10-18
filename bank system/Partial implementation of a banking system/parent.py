class Parent:
    
    def __init__(self,fname,lname,address):
        self.fname = fname
        self.lname = lname
        self.address = address
        
    def update_first_name(self, fname):
        self.fname = fname
    
    def update_last_name(self, lname):
        self.lname = lname
                
    def get_first_name(self):
        return self.fname
    
    def get_last_name(self):
        return self.lname
    
    def update_address(self):
        num = str(input( "House number:" ))
        street = str(input( "Street name:" ))
        city = str(input( "City:" ))
        pc = str(input( "Post code:" ))
        addr = [num,street,city,pc]
        self.address = addr
                
    def get_address(self):
        return self.address
    