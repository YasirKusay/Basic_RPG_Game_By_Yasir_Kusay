import random
from map_funs import *
from char_class import *
from fight_funs import *
from time import sleep

# map will be a 2d list of dictionaries
# each dictionary will contain an item, an obstacle or an opponent and if the player character is in the location

def process_location(direction, player):
    print(f"moving {direction}")
    print(move(yasir, direction))
    if survey_position(player) == "dead":
        return "dead"

def main_fun():
    global yasir
    yasir.position = (1, 1)
    john.position = (0, 1)
    jake.position = (2, 2)
    # print(move(yasir, "left"))
    '''
    print(move(yasir, "up"))
    assert game_map[1][0]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "up"))
    assert game_map[1][0]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "down"))
    assert game_map[1][1]["player"] == True
    assert game_map[1][0]["player"] == False
    print(move(yasir, "down"))
    assert game_map[1][2]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "down"))
    assert game_map[1][2]["player"] == True
    print(move(yasir, "up"))
    assert game_map[1][1]["player"] == True
    assert game_map[1][2]["player"] == False

    print("            TESTING LEFT RIGHT              \n")

    print(move(yasir, "left"))
    assert game_map[0][1]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "left"))
    assert game_map[0][1]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "right"))
    assert game_map[1][1]["player"] == True
    assert game_map[0][1]["player"] == False
    print(move(yasir, "right"))
    assert game_map[2][1]["player"] == True
    assert game_map[1][1]["player"] == False
    print(move(yasir, "right"))
    assert game_map[2][1]["player"] == True
    print(move(yasir, "left"))
    assert game_map[1][1]["player"] == True
    assert game_map[2][1]["player"] == False
    '''

    '''
    survey_position(yasir)
    move(yasir, "up")
    survey_position(yasir)
    '''
    #yasir.status = "Confused"
    while True:
        command = input("What would you like to do?")
        if command == "left" or command == "right" or command == "up" or command == "down":
            if process_location(command, yasir) == "dead":
                return "dead"
        elif command.startswith("equip") == True:
            print(equip(command, yasir))
        elif command.startswith("take"):
            take(command, yasir)
        else:
            print("unknown command")

main_fun()