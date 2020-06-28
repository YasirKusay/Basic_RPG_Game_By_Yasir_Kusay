import random
from fight_funs import get_experience

class character:
    def __init__(self, name, level, npc):
        self.name = name
        self.health = 100
        self.level = level
        self.attack_hitpoints = 0
        if level != 1:
            self.attack_hitpoints = 10 + level
        else:
            self.attack_hitpoints = 10
        self.status = "alive"
        self.inventory = [] # holds enhancement potions, healing potions, armaments
        self.successful_attacks = 0
        self.attack_experience = 0
        self.max_health = 10
        if level != 1:
            self.max_health = 100 + level
        else:
            self.max_health = 100
        self.armour = None
        # self.sword = "Sword of Confusion"
        self.sword = None
        self.status = "Compitent" # two status, compitent and confused, confused means less likely to land a hit
        self.npc = npc # NPC Status
        self.position = None

    def level_up(self):
        if (get_experience(self.level + 1) <= self.attack_experience):
            print(f"{self.name} has levelled up! They are now level {self.level}!")
            self.max_health += self.max_health + 1
            self.level += 1
            self.attack_hitpoints += 1
    
    def attack(self, player):
        if self.status == "Confused":
            if random.randint(0, 100) >= 50:
                print("successful attack!")
                attack_damage = 0
                if self.sword == "great sword":
                    attack_damage = (self.attack_hitpoints*2)
                    player.health -= attack_damage
                else: 
                    attack_damage = self.attack_hitpoints
                    player.health -= attack_damage
                self.attack_experience += attack_damage
                self.level_up()
                self.check_confused(player)
            else:
                print("missed!")
        else:
            if random.randint(0, 100) >= 30:
                print("successful attack!")
                attack_damage = 0
                if self.sword == "great sword":
                    attack_damage = (self.attack_hitpoints*2)
                    player.health -= attack_damage
                else: 
                    attack_damage = self.attack_hitpoints
                    player.health -= attack_damage
                self.attack_experience += attack_damage
                self.level_up()
                self.check_confused(player)
            else:
                print("missed!")
            
        if self.npc == True:
            print(f"your health is {player.health}")
        elif self.npc == False:
            print(f"the enemy's health is {player.health}")
                
    def check_confused(self, player):
        if self.sword == "sword of confusion":
            if random.randint(0, 4) == 2:
                player.status = "Confused"
                if self.npc == True:
                    print("You are confused!")
                else:
                    print("Opponent is confused!")   


list_of_characters = []