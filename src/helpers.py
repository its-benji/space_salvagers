from prompt_toolkit import prompt
from character import *
from weapon import *
import random

def next_action(choices, text):
    key=''
    while key not in choices:
        print(text)
        # print out all player choices
        for key in choices:
            print(key)
        key = prompt()
        if key not in choices:
            print("Not a valid choice - please try again.")
    return key

def set_order(p1: Character, p2: Character):
    print(p1.weapon.speed)
    
def combat_round(p1, p2):
    return None

        