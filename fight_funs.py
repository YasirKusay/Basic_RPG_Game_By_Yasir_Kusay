import char_class

def get_experience(level):
    sum = 0
    i = 1
    while i <= level - 1:
        sum = sum + (1/4)*(i + (300*(2**(i/7))))
        i += 1
    return sum        

def equip(item, player):
    equipment = item.split(" ")
    i = 1
    sword = None
    while i < len(equipment):
        if i == 1:
            sword = equipment[i]
        else:
            sword = sword + " " + equipment[i] 
        i += 1

    if sword in player.inventory:
        player.sword = sword
        return sword + " " + "equipped"
    else:
        print("you do not have that item!")
        return "nothing equipped"

def take(item, player):
    equipment = item.split(" ")
    i = 1
    potion = None
    while i < len(equipment):
        if i == 1:
            potion = equipment[i]
        else:
            potion = potion + " " + equipment[i] 
        i += 1

    if potion in player.inventory:
        if potion == "health potion":
            player.inventory.remove(potion)
            if (player.health + 50) > player.max_health:
                    player.health = player.max_health
            else:
                player.health += 50
            print(f"You're health is now {player.health}")
        elif potion == "anti confusion":
            player.status = "Compitent"

    else:
        print("you do not have that item!")
        return "nothing equipped"   
            
def fight(opponent1, opponent2):
    print(f"{opponent2.name} wants to battle!")
    print(f"they are level {opponent2.level}!")
    while opponent1.health >= 0 or opponent2.health >= 0:
        if opponent1.health <= 0:
            opponent1.health = 0
            opponent1.status = "deceased"
            print("you are dead!")
            return "dead"

        while True:
            action = input("What are you going to do?")
            if action == "run":
                print("Got away safely!")
                return "escaped"
            elif action == "attack":
                opponent1.attack(opponent2)
                break
            elif action == "take anti confusion":
                # check if you have that elixer
                take("take anti confusion", opponent1)
                '''
                opponent1.status = "Compitent"
                print("You are no longer confused!")
                '''
                break
            elif action == "take health potion":
                # check if you have health potion
                take("take health potion", opponent1)
                '''
                if (opponent1.health + 50) > opponent1.max_health:
                    opponent1.health = opponent1.max_health
                else:
                    opponent1.health += 50
                print(f"You're health is now {opponent1.health}")
                '''
                break
                
            else:
                print("unknown move!")
        
        if opponent2.health <= 0:
            opponent2.health = 0
            opponent2.status = "deceased"
            print("you win!")
            return "alive"
        
        # print("oponent 2 is ready to attack", end="\r")
        print("opponent 2 is ready to attack")
        opponent2.attack(opponent1)