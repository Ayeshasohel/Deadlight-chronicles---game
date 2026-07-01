class Character():
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
        self.points = 0 
        self.personal_item = None
        
    def describe(self):
        print(self.name + " is here!" )
        print(self.description )
     
    def set_conversation(self, conversation):
        self.conversation = conversation
    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")
    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
    
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None
    
        
class Enemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def set_weakness(self, weapon_weaknesses):
        self.weakness = weapon_weaknesses
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You defeat " + self.name + " the master of demons with " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        
    def set_health(self, health_points):# not in use 
        self.health = health_points
    
    def get_health(self):# not in use
        return self.health
    

class Aenemy(Character):
    enemies_to_defeat = 0
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None
        Enemy.enemies_to_defeat = Enemy.enemies_to_defeat + 1

    def set_weakness(self, weapon_weaknesses):
        self.weakness = weapon_weaknesses
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You scare " + self.name + " with " + combat_item )
            Enemy.enemies_to_defeat = Enemy.enemies_to_defeat - 1
            return True
        else:
           print(self.name + " swallows you, little wimp")
           return False 
    def loot(self):
        print(f"You stole {self.personal_item.get_name()} from {self.name}!")

        
    def set_personal_item(self, item):
        self.personal_item = item

    def steal(self):
        if self.personal_item:
            print(f"You stole {self.personal_item.get_name()} from {self.name}!")
            stolen_item = self.personal_item
            self.personal_item = None
            return stolen_item
        else:
            print(f"{self.name} has nothing to steal.")
            return None

class Friend(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def cook(self):
        print(self.name + " makes meat for you to increase your health")
    def steal(self):
        print("well someone's looking for trouble")
    def attack(self):
        print("PLaying offence, I like it!")
    def help(self):
        print("DEFENCE! PROPOSTROUS")

class Bystander(Character):
    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.feeling = None
    def talk(self):
        print("No one wants to talk to a HUMAN")