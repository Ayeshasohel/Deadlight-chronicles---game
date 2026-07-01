class Weapon:
    def __init__(self, name):
        self.name = name 
        self.description = None

    def set_description(self, description):
        self.description = description
 
    def get_description(self):
        return self.description
    
    def set_name(self, weapon_name):
        self_name = weapon_name

    def get_name(self):
        return self.name
     
    def describe(self):
        print (f"The [{self.name}] is here - {self.description}")
    

