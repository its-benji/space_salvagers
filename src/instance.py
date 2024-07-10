from character import *
from prompt_toolkit import prompt
from helpers import *
from weapon import *
import time

class Room:
    def __init__(self, routes, text, hasCrate=False):
        self.entities = {}
        self.items = []
        self.weapons = []
        self.hasCrate = hasCrate
        self.text = text
        self.routes = routes

    def add_entity(self, entity):
        self.entities[entity.name] = entity

    # when an entity dies
    def remove_entity(self, entity):
        del self.entities[entity.name]

    def add_items(self, items):
        self.items = items
    
    def remove_item(self, item):
        self.items.remove(item)

    def add_weapons(self, weapons):
        self.weapons = weapons
    
    def remove_weapon(self, weapon):
        self.weapons.remove(weapon)
    

    '''
    create the routing for walking through rooms
    '''


class Instance:
    def __init__(self):
        weapon_list = ['BLASTER', 'PHASE_BLADE', 'PULSE_RIFLE']
        self.salvage_found = False
        self.rooms = {
                "armory": Room({'go_back':'corridor_1_0'}, "\nIt looks like an old armory.", True),
                "room_0_0": Room({"go_left": "room_0_1", "go_forward":"corridor_1_0"}, "\nYou step into the room. Other than some blasterfire on the walls, it's empty."),
                "room_0_1": Room({'go_back':'room_0_0'}, "\nYou find yourself in a small compartment, empty, except for a crate in the corner.", True),
                "corridor_1_0": Room({'go_forward':'armory', 'go_back':'room_0_0'}, "\nYou step into the corridor.")
            }
        
        self.rooms['armory'].add_weapons(weapon_list)
        self.rooms['room_0_1'].add_items(['STIM'])
        self.rooms['corridor_1_0'].add_entity(CharacterFactory('SPACE_PIRATE', 'Dooley'))

        
        '''
        prompt user for character name
        '''
        name = prompt("Kaydin: What's your name, kid? \n")
        self.player = CharacterFactory('PLAYER', name)
        # Opening Scene
        if False:
            name = prompt("Kaydin: What's your name, kid? \n")
            self.player = CharacterFactory('PLAYER', name)
            time.sleep(1)
            print(f"Kaydin: {name}, huh? This your first salvage run? You'll be a pile of goo if you go in like that. Grab something from the rack over there!")
            time.sleep(3)
            weapon = event(weapon_dict, "Choose a weapon by typing in the corresponding number: \n 1. Blaster \n 2. Phase Blade \n 3. Pulse Cannon\n")
            self.player.change_weapon(WeaponFactory(weapon_dict[weapon]))
            time.sleep(0.5)
            print("Kaydin: Nice choice! Now, let's get moving.")
            time.sleep(1.5)
            print('\nYou follow Kaydin through the ship, and soon find yourself in a cramped docking compartment with two other humanoids.')
            time.sleep(3)
            print('\nThey look a little scary. You wonder what you\'ve gotten yourself into.')
            time.sleep(3)
            print('\nKaydin: Right, listen up, we go in quick and we get out quick. We get this right, we\'ll be sipping ' +
                'sliders on some distant ocean world with more cred-chips then we know how to spend.')
            time.sleep(5)
            print('\nThe others cheer. You join in.')
            time.sleep(3)
            print('There\'s a heavy thunk outside, and a minute later the hatch opens up, leading to the ship you\'re about to salvage.')
            time.sleep(3)
            print('You follow the others into a dark, empty corridor.')
            time.sleep(2.5)
            print('Kaydin: Drax, you and I hit up the cargo-hold. Krug, you\'re on crew cabins.')  
            time.sleep(2)
            print('Kaydin turns to you.')
            time.sleep(2)
            print('Kaydin: New kid... see what they\'ve got in their bridge.')
            time.sleep(3)
            print('Krug: What about survivors?')  
            time.sleep(2)
            print('Kaydin pats his blaster')
            time.sleep(2)
            print('Kaydin: You know what to do.')
            time.sleep(0.5)
            print('* ', end=" ")
            time.sleep(0.5)
            print('*')
            time.sleep(0.5)
            print('* ')
            time.sleep(0.5)


        print('\nYou go the opposite direction as the others. At the end of the corridor you come to a door.')
        time.sleep(2.5)
        print('\nThere\'s streaks across the battered metal. They look a little like claw marks.')
        time.sleep(2.5)
        print('There\'s a panel to your right. You tap it, and the door slides open.')
        time.sleep(3)

        alive = True
        self.current_room = "room_0_0"
        while alive: 
            print(self.rooms[self.current_room].text)

            if self.rooms[self.current_room].entities:
                set_order(self.player, self.player)
            
            options = list(self.rooms[self.current_room].routes.keys())
            if self.rooms[self.current_room].hasCrate:
                options = options + ['open_chest']
            action = next_action(options, "Choose an action: ")

            if action == 'open_chest':

                if len(self.rooms[self.current_room].items) == 0:
                    print('Chest is Empty')
                else:
                    item = next_action(self.rooms[self.current_room].items, 'Choose an item to take: ')
                    self.player.add_stim()
                    self.rooms[self.current_room].remove_item(item)

            if action in self.rooms[self.current_room].routes:
                self.current_room = self.rooms[self.current_room].routes[action]
            
        


            

        '''
        further commands here
        '''

        '''
        for now just treat this as the script of the instance, you can abstract
        it once it is working
        '''

