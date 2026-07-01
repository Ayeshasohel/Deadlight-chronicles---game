class Passage: 
    def __init__(self, passage_name):
        self.name = passage_name
        self.description= None
        self.linked_passages = {}
        self.character = None
        self.weapon = None
    def get_weapon(self):
        return self.weapon
    def set_weapon(self, weapon_name):
        self.weapon = weapon_name
 
    def set_description(self, passage_description):
        self.description = passage_description

    def get_description(self):
        return self.description
    
    def set_name(self, passage_name):
        self_name = passage_name

    def get_name(self):
        return self.name

    def set_character(self, new_character):
        self.character = new_character
        
    def get_character(self):
        return self.character
    
    def describe(self):
        print(self.description)

    def link_passage(self, passage_to_link, direction):
        self.linked_passages[direction] = passage_to_link

    def move(self, direction):
        if direction in self.linked_passages:
            print(f"Moving {direction}...")
            return self.linked_passages[direction]
        else:
            print("You can't go that way")
            return self

    def get_details(self):
        print(self.name)
        print("⚔⚔⚔⚔⚔⚔⚔⚔")
        print(self.description.upper())
        for direction in self.linked_passages:
            passage = self.linked_passages[direction]
            print("The " + passage.get_name() + " is " + direction)
            
