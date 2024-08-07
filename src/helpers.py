from prompt_toolkit import prompt
from prompt_toolkit.styles import Style
from character import *
from room import Room
from weapon import *
import sys
import time

style = Style.from_dict({
            'prompt': '#ff0066',  # user text color
        })

def dots():
    time.sleep(.5)
    print('  .  ', end='')
    sys.stdout.flush()
    time.sleep(.5)
    print('  .  ', end='')
    sys.stdout.flush()
    time.sleep(.5)
    print('  .  ')
    sys.stdout.flush()
    time.sleep(.5)
    
def slow_dots():
    time.sleep(1)
    print('  .  ', end='')
    sys.stdout.flush()
    time.sleep(1)
    print('  .  ', end='')
    sys.stdout.flush()
    time.sleep(1)
    print('  .  ')
    sys.stdout.flush()
    time.sleep(1)

def next_action(choices: list[str], text):
    key=''
    while key not in choices:
        print(text)
        # print out all player choices
        for key in choices:
            print(key)
        key = prompt(style=Style.from_dict({'': 'ansiyellow'}))
        if key not in choices:
            print("\033[31mNot a valid choice - please try again.\033[0m")
    return key

def search_room(choices: list[str]):
    if len(choices) == 1:
        print('\n'+choices[0])
    else:
        i = 0
        key = ''
        
        while key != 'finish':
            if i == 0: 
                key = next_action(['next'], choices[i])
                i+=1
            elif i == len(choices)-1:
                key = next_action(['prev', 'finish'], choices[i])
                i-=1
            else:
                key = next_action(['prev', 'next'], choices[i])
                if key == 'next':
                    i+=1
                else:
                    i-=1 
            if key != 'finish':
                dots()
                    
    
def draw_map(location):
    print('            _____        ')
    print('        ___/     \___     ')
    print('       /     [=]     \  ')
    print('      |               |  ')
    print('     / control-bridge  \  ')
    print('    /                   \ ')
    print('    |_______     _______| ')
    print('            |   |         ')
    print('            |C-3|         ')
    print('     _____  |   |  _____  ')
    print('   / [=]  \_|   |_/  [=] \ ')
    print('  |  ST-3  _     _  ST-9  | ')
    print('   \_    _| \___/ \_    _/ ')
    print('     |  |           |  |   ')
    print('    _|  |___________|  |_  ')
    print('   |                     | ')
    print('   |       lab-2         | ')
    print('   |________,   ,________|')
    print('    ________|   |        ')
    print('   |   C-2      |        ')
    print('   |    ________|        ')
    print('   |   |      __________ ')
    print('  _|   |__   |    [=]   |')
    print(' |        |__|          |')
    print(' |  lab-1  __   armory  |')
    print(' |________|  |          |')
    print('             |___,   ,__|')
    print('                 |   |   ')
    print('                 |C-1|   ')
    print('                 |   |   ')
    print('              ___|   |__ ')
    print('     ______  |          |')
    print('    |ST-47 |_|          |')
    print('    |       _    YV-4   |')
    print('    |_[=]__| |          |')
    print('             |__, ,_____|')
    print()
    print(f'Current Room:   \033[31m{location}\033[0m')
    print('Chest:          [=]')