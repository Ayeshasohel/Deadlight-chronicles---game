class Ship:
    def __init__(self, ship_name): 
        self.name = ship_name
        self.description= None
        self.linked_ships = {}
        self.character = None
        self.weapon = None

    def get_weapon(self):
        return self.weapon
     
    def set_weapon(self, weapon_name):
        self.weapon = weapon_name

    def set_description(self, ship_description):
        self.description = ship_description

    def get_description(self):
        return self.description
    
    def set_name(self, ship_name):
        self_name = ship_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character
        
    def get_character(self):
        return self.character
    
    def describe(self):
        print(self.description)

    def link_ship(self, ship_to_link, direction):
        self.linked_ships[direction] = ship_to_link

    def jump(self, direction):
        if direction in self.linked_ships:
            ship = self.linked_ships[direction]
            print("Jump onto " + ship.get_name())
            return self.linked_ships[direction]

    def get_details(self):
        print(self.name)
        print(self.description)
        print("☠️ ☠️ ☠️ ☠️")
        for direction in self.linked_ships:
            ship = self.linked_ships[direction]
            print("You can jump or run but be quick on your feet")
            print("Next stop: " + ship.get_name())
            

