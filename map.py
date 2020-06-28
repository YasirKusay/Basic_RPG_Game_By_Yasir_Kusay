from char_class import *
from my_game import *

MAX_HEIGHT = 2
MAX_WIDTH = 2

yasir = char_class.character("yasir", 1, False)
# yasir.sword = "Great Sword"
# yasir.sword = "Sword of Confusion"
john = char_class.character("john", 1, True)
# john.status = "Confused"
# john.sword = None
jake = char_class.character("jake", 100, False)
jake.sword = "Great Sword"
# print(fight_funs.fight(yasir, john))
    
w = 3
h = 3
game_map = [[0 for x in range(w)] for y in range(h)] 
game_map[0][0] = {"position": (0, 0), "opponent": None, "item": "Great Sword", "obstacle": None, "player": False}
game_map[0][1] = {"position": (0, 1), "opponent": john, "item": None, "obstacle": None, "player": False}
game_map[0][2] = {"position": (0, 2), "opponent": None, "item": None, "obstacle": "bronze ore", "player": False}
game_map[1][0] = {"position": (1, 0), "opponent": None, "item": "Pickaxe", "obstacle": None, "player": False}
game_map[1][1] = {"position": (1, 1), "opponent": None, "item": None, "obstacle": None, "player": True}
game_map[1][2] = {"position": (1, 2), "opponent": None, "item": None, "obstacle": "Furnace", "player": False}
game_map[2][0] = {"position": (2, 0), "opponent": None, "item": None, "obstacle": None, "player": False}
game_map[2][1] = {"position": (2, 1), "opponent": None, "item": None, "obstacle": None, "player": False}
game_map[2][2] = {"position": (2, 2), "opponent": jake, "item": "Great Sword", "obstacle": None, "player": False}


def get_player_position(player):
    i = 0
    while i < MAX_WIDTH:
        j = 0
        while j < MAX_HEIGHT:
            if game_map[i][j]["player"] == True:
                player.position = game_map[i][j]["position"]
                return game_map[i][j][position]
            j += 1
        i += 1

def move(player, direction):
    # if direction = 
    global game_map
    (i, j) = get_player_position(player)
    while True:
        if direction == "left":
            if i == 0:
                print("You will go out of bounds!")
                return "not moved"
            else:
                game_map[i][j]["player"] == False
                game_map[i-1][j]["player"] == True
                player.position = (i-1, j)

        if direction == "right":
            if i == MAX_WIDTH:
                print("You will go out of bounds!")
                return "not moved"
            else:
                game_map[i][j]["player"] == False
                game_map[i+1][j]["player"] == True
                player.position = (i+1, j)

        if direction == "up":
            if j == 0:
                print("You will go out of bounds!")
                return "not moved"
            else:
                game_map[i][j]["player"] == False
                game_map[i][j-1]["player"] == True
                player.position = (i, j-1)
        
        if direction == "down":
            if i == HEIGHT:
                print("You will go out of bounds!")
                return "not moved"
            else:
                game_map[i][j]["player"] == False
                game_map[i][j+1]["player"] == True
                player.position = (i, j+1)
        


def survey_position(player):
    # global 
    (i, j) = player.position 
    if game_map[i][j]["opponent"] != None:
        opponent = game_map[i][j]["opponent"]
        print(f"You have encountered {opponent}!")
        fight_return = fight(player, opponent)
        if fight_return == "alive":
            game_map[i][j]["opponent"] = None
            assert game_map[i][j]["opponent"] == None
            return "alive"

        # elif fight_return == "escaped":

        else:
            print("You are dead")
            return "dead"    
    
    if game_map[i][j]["item"] != None:
        item = game_map[i][j]["item"]
        print(f"You have found {item}")
        while True:
            respone = input("Do you want to pick it up?")
            if response == "yes":
                player.inventory.append(item)
                game_map[i][j]["item"] = None
                break

            elif response == "no":
                break
        
    if game_map[i][j]["obstacle"] != None:
        obstacle = game_map[i][j]["obstacle"]
        print(f"You have encountered a {obstacle}!")
        if obstacle == "bronze ore":
            while True:
                response = input("Would you like to mine it?")
                if response == "yes":
                    if "pickaxe" in yasir.inventory:
                        player.inventory.append("bronze ore") 
                        game_map[i][j]["obstacle"] = None
                        break
                    
                    else:
                        print("You do not have a pickaxe to mine the rocks!")
                        break

                elif response == "no":
                    break
        
        if obstacle == "furnace":
            while True:
                response = input("Would you like to make a weapon?")
                if response == "yes":
                    if "bronze ore" in yasir.inventory:
                        player.inventory.append("sword of confusion") 
                        break
                    
                    else:
                        print("You do not have raw materials to use!")
                        break

                elif response == "no":
                    break
