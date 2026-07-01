import time
from passage import Passage
from char import Enemy, Friend, Aenemy, Bystander
from weapon import Weapon
from ship import Ship
  
def play_game():
    print("               ")
    print("You have fallen to your destruction - Welcome to the Gothic tale")
    print("Greetingssss you low-life Human....")
    print("It is time for you to play ssssurvival....")
    print("ANIHILATE the demon of thissss realm that you will find him in the GRIM HALL.....")
    print("CHOOSE wisely mud-blood your life dependssss on it....")
    darkmaw = Passage("Dark maw")
    darkmaw.set_description("The path that leads to perpetual oblivion")
    grimhall = Passage("Grimhall") 
    grimhall.set_description("The hall of the dead")
    nightveil = Passage("Nightveil")
    nightveil.set_description("A twilight path where lingers the agony")
    nightveil.set_description("HAA... MORON, THERE IS NOTHING HERE TO SIGHT SEE until...")
    hollowpass = Passage("Hollowpass")
    hollowpass.set_description("A black hole, where the living seize to exist")
    
    darkmaw.link_passage(grimhall, "south")
    nightveil.link_passage(grimhall, "east")
    grimhall.link_passage(nightveil, "west")
    grimhall.link_passage(darkmaw, "north")
    grimhall.link_passage(hollowpass, "across")
    hollowpass.link_passage(grimhall, "east")

    gojo = Enemy("Gojo", "A smug Demon")
    gojo.set_conversation("Dare to fight me, you weakling")
    gojo.set_weakness("Cursed sword")
    grimhall.set_character(gojo)

    seyfi = Bystander("SEYFI", "A useless, needy creature....You can talk to me if you want to")
    nightveil.set_character(seyfi)

    chris = Friend("Chris", "An extraordinary cook")
    chris.set_conversation("Mamamia")
    darkmaw.set_character(chris)

    egg = Weapon("EGG")
    egg.set_description("A demon's weakness")
    hollowpass.set_weapon(egg)

    chest = Weapon("The Elder wand")
    chest.set_description("A flame in the dark")
    grimhall.set_weapon(chest)

    sword = Weapon("Cursed sword")
    sword.set_description("The ultimate death of any Enemy")#change name to cursed sword in all code

    bag = []
    current_passage = darkmaw
    dead = False 
    points = 0
    print("LEVEL 1")
    while not dead:
        print("\n")         
        current_passage.get_details()
        weapon = current_passage.get_weapon()
        inhabitant = current_passage.get_character()
        if weapon:
            weapon.describe()
        if inhabitant:
            inhabitant.describe() 
        print("Loot, Open, steal.... and a weapon would be yours")
        if inhabitant is not None and isinstance(inhabitant, Friend):
            start_time = time.time()
            command = input(">")
            elapsed_time = time.time() - start_time
            if elapsed_time > 4 and command != "eat":
                print("(Hint: You can try using 'eat' to increase your health points!)")
        else:
            command = input(">")
        if points >= 20 and "Cursed sword" not in bag:
            print("✨ You've unlocked the Cursed sword! ✨")
            bag.append("Cursed sword")   
        if command in ["north", "south", "east", "west", "across"]:
                current_passage = current_passage.move(command)
        elif command == "talk":
            if inhabitant:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Enemy):
                required_item = ["Cursed sword", "The Elder wand", "EGG"]
                if all(weapon in bag for weapon in required_item):
                # Fight with the inhabitant, if there is one
                    print("What will you fight with?")
                    print(bag)
                    fight_with = input()
                    if fight_with == "EGG":
                        print("Gojo's heart has melted from the EGG")
                        print("You get another chance to fight off the Demon")
                        continue
                    if fight_with in bag:
                        if inhabitant.fight(fight_with) == True:
                            # What happens if you win?
                            current_passage.set_character(None)
                            if Enemy.enemies_to_defeat == 0:
                                print("Congratulations, you have survived another adventure")
                                replay = input("Do you want to move onto the next level? (yes/no)? ".lower())
                                if replay == "yes":
                                    return True
                                else:
                                    print("Thank you for playing")
                                    return False
                        else:
                            print("That's the end of the game")
                            dead = True
                    else:
                        print("You don't have a " + fight_with)
                else:
                    print("You don't have all the weapons yet")
            else:
                print("You ghastly creasture, Can't you see there is no one here to fight with!")
        elif command == "steal": # not working code
            if weapon is not None:
                print("You put the " + weapon.get_name() + " in your bag")
                bag.append(weapon.get_name())
                current_passage.set_weapon(None)
            else:
                print("There is nothing here to steal :(")
        elif command == "eat":
            if inhabitant is not None:
                if isinstance(inhabitant, Friend):
                    inhabitant.cook()
                    points += 10
                    print("You have increased health by 10 points! Total:", points)
        elif command == "loot":
            if weapon is not None:
                print("You put the " + weapon.get_name() + " in your bag")
                bag.append(weapon.get_name())
                current_passage.set_weapon(None)
        elif command == "open":
            if chest is not None:
                print("You have attained the mystery item")
                print("The Elder wand")
                bag.append(chest.get_name())
                current_passage.set_weapon(None)


def play_game2():
    print("               ")
    print("Ahoyyyyy mateyyy... Welcome to level 2 - The Phantom Ships")
    print("Scallywag, tell me your name")
    name = input()
    print(name + "You are on a blissful journey to win back the Phantom ships from the Archenemy and the tyrant king of the ships - LUCA")
    print("Play wisely or it might cose a pirate's dignity")
    caribbean = Ship("Caribbean")# anara = caribbean
    caribbean.set_description("A vessel with secrets and spilled rum")
    piratehaven = Ship("Pirate haven")# dungeon = pirate haven
    piratehaven.set_description("A pirates place to steal, sail and sleep")
    republican = Ship("Republican")# grotto = republican
    republican.set_description("A polished history with pirates stabbing backs")
    crossfire = Ship("Cross Fire")# grotto = republican
    crossfire.set_description("Filled with unrelentless snakes waiting to show their true colours")
    
    caribbean.link_ship(republican, "jump")
    republican.link_ship(piratehaven, "jump")
    piratehaven.link_ship(crossfire, "jump")

    crystal = Friend("Crystal", "A Deck diva")
    crystal.set_conversation("Aye Aye captain")
    caribbean.set_character(crystal)
    republican.set_character(crystal)
    piratehaven.set_character(crystal)
    crossfire.set_character(crystal)

    Luca = Aenemy("Luca", "The Archenemy")
    Luca.set_conversation("Human....Fooood")
    crossfire.set_character(Luca)
    circle = Weapon("White circle")
    circle.set_description("A cursed ring")
    crossfire.set_weapon(circle)
    Luca.set_personal_item(circle)

    key = Weapon("Goblin's key")
    key.set_description("Shining emeralds, Every pirate's dream")
    caribbean.set_weapon(key)

    goblet = Weapon("Golden goblet")
    goblet.set_description("Saphires glistening the tained rim")
    republican.set_weapon(goblet)

    star = Weapon("Death star")
    star.set_description("The ultimate death of any Enemy")
    piratehaven.set_weapon(star)
    
    bag2 = []
    current_ship = caribbean 
    dead = False 
    strength = 0
    Aenemy_strength = 5
    print("LEVEL 2")
    while not dead:
        print("\n")         
        current_ship.get_details()
        weapon = current_ship.get_weapon()
        inhabitant = current_ship.get_character()
        print("Steal, Attack, Help.... and a weapon would be yours")
        if weapon:
            weapon.describe()
        if inhabitant:
            inhabitant.describe() 
        command = input(">")    
        if command in ["jump"]:
            current_ship = current_ship.jump(command)
        elif command == "talk":
            if inhabitant:
                inhabitant.talk()
        elif command == "fight":
            if inhabitant is not None and isinstance(inhabitant, Aenemy):
                required_weapons = bag2# not working yet
                if all(req.lower() in [item.lower() for item in bag2] for req in required_weapons):
                    print(bag2)
                    print("Swabbieeee, You've overpowered Archenemy Luca, victory is yours")
                    print("You have crushed the ultimate finale. CONGRATULATIONS")
                    print("You have completed your mission and have finally achieved your rightful title")
                    print("ALL HAIL" + name + "the leader of the Phantom ships")
                    print("You have yet to proof yourself by strength")
                    dead = True
                elif strength > Aenemy_strength: # important code, continue with printing that you have won, and else statement if you have lost
                    Aenemy.enemies_to_defeat == 0
                    print("Shiver me timbers!!! arrrrmazing play, someone's finally won")
                    print("Well, impressive play matey")
                    print("You have completed your mission and have finally achieved your rightful title")
                    print("ALL HAIL" + name + "the leader of the Phantom ships")
                    print("Yor have prove yourself worthy for the title")
                    print("Congratulaitions")
                    dead = True
                else: 
                    print("IMBECILE, Master luca has crushed you with his strength")
                    print("You have failed to eliminate the leader of - The Phantom ships")
                    print("You are a shame for your crew mates and a disappointment")
                    print("You are hereby banished from the ships")
                    dead = True
            else:
                print("Blimeyyy, bilge rat, there is no one here to fight with")  
        elif command == "steal":
            if inhabitant is not None and weapon not in bag2:
                if isinstance(inhabitant, Friend):
                    strength +=  0.5
                    print("You have attained 0.5-star stregth! Total:", strength)
                    bag2.append(weapon.get_name())
                    current_ship.set_weapon(None)
        elif command == "loot":
            if isinstance(inhabitant, Aenemy):
                if weapon is not None:
                    bag2.append(weapon.get_name())
                    print(f"You have stolen {weapon.get_name()}!")
        elif command == "attack":
            if weapon is not None:
                strength +=  2
                print("You have attained 2-star stregth! Total:", strength)
                bag2.append(weapon.get_name())
                current_ship.set_weapon(None)
        elif command == "help":
            if inhabitant is not None and weapon not in bag2:
                if isinstance(inhabitant, Friend):
                    bag2.append(weapon.get_name())   
                    inhabitant.help()
                    strength += 3
                    print("You have attained 3-star stregth! Total:", strength)
                    current_ship.set_weapon(None)# add what is in the bad and say choose wisely, let the inhabitant pick and win or lose.
        if command in ["run"]:
            print("You incompetent coward")
            current_ship = current_ship.jump("jump")
        if command in ["steal", "attack", "help"]:
            current_ship = current_ship.jump("jump")

while True:
    continue_game = play_game()
    if continue_game:
        play_game2()
    break