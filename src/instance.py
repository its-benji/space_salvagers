from character import *
from prompt_toolkit import prompt, HTML
from prompt_toolkit.styles import Style
from helpers import *
from combat import *
from weapon import *
from room import *
import time
from scenes import *


class Instance:
    def __init__(self):
        self.salvage_found = False
        self.power_switch = False
        self.rooms = {
                "armory": Room({'go_back':'c_1', "go_left":'lab_1'}, "\nIt looks like an old armory.", ['There\'s weapons and ammo-packs strewn across the deck - whoever was in here left in a hurry.'], '', True),
                "YV-4": Room({"go_left": "ST-47", "go_forward":"c_1"}, 
                             "\nYou step into the room. On either side of you are empty bunks.", 
                             ['On one of the bunks you find a digi-tab. You flick it open.', 
                              'Log 052: Day 47 of this hellish voyage. Strange noises in the lab continue - shrieks and screams that make your skin crawl. Valya complained to the Sci-Tech gearheads, \nsaid they need to let us know what\'s going on in our own ship. Said we\'d mutiny if they did\'t. Never should have left Albios.',
                              "Log 053: Sci-Tech agreed to let one of us in. Valya chosen - will at last find out what they're up to. Still don't trust Sci-Tech. Bridge pass-key changed to \033[31m1337\033[0m as precaution in case they try to take the ship.",
                              "Log 054: Day 48. Valya infected in their lab - taken directly to med-bay before she could explain. Lab-techs won't let me see her. Noises continued last night. Sounded like human screams. Have to get off this blasted ship.",
                              "Log 055: Valya not in med-bay. Never was. Security footage shows she never left lab. We're arming up and going in after her. Once she's free from those sick-minded gear-heads, \nwe're changing course to the nearest habited planet. Will update again tonight.\n",
                              "There are no further logs. You flick off the digi-tab and return it to its bunk."],
                             "\n*** COMM-MESSAGE ***.\nKaydin: Hey kid! Mako just picked up some activity in your section. Looks like some space-pirates beat us to the haul. Blasters at the ready. \n*** END-COMM ***", False, True),
                "ST-47": Room({'go_back':'YV-4'}, "\nYou find yourself in a small compartment, empty except for a storage crate to your left.", ['The compartment appears to be empty.'], '', True),
                "ST-3": Room({'go_back':'lab_2', "go_right": "c_3"}, "\nYou find yourself in a small compartment, empty except for a storage crate to your left.", ['The compartment appears to be empty.'], '', True),
                "ST-9": Room({'go_back':'lab_2', "go_left": "c_3"}, "\nYou find yourself in a small compartment, empty except for a storage crate to your left.", ['The compartment appears to be empty.'], '', True),
                "c_1": Room({'go_forward':'armory', 'go_back':'YV-4'}, "\nYou step into the corridor.", ['The space-pirate lies slumped against the wall.'], ''),
                "lab_1": Room({"go_right": "armory", "go_forward":"c_2"}, 
                             "\nYou step into a labratory filled with smashed control panels, analytics screens, and human-sized vats.", 
                             ['One of the screens is still intact. You tap into the screen, and a video-log begins to play.', 
                              'Log 212: Another setback. Injection was successful, but once again the subject went berserk and nearly destroyed lab-1.',
                              "Log 233: Crew is getting restless. So is Syphon. Running out of subjects. Running out of time.",
                              "Log 237: Crew demanded to be let into lab. Perhaps this is our solution? We could never let her out alive anyways.\nSyphon wouldn't allow it. Crew member is 31 years old. Human. Female.",
                              "Log 240: Injection never performed on human before, but out of options. Experiment commencing at 0900 hours."],
                             ""),
                "c_2": Room({'go_forward':'lab_2', 'go_back':'lab_1'}, "\nYou step into a corridor.", ['The space-pirate lies slumped against the wall.'], "\nSuddenly, two space-pirates charge around the corner at the end. \n Run! Get out of here! They shout as they run past you.", False, True),
                "c_3": Room({'go_left':'ST-3', 'go_right':'ST-9', 'go_forward':'control_bridge'}, "\nYou step into a corridor.", ['The Space-Pirate lies crumpled against the wall.'], ''),
                "lab_2": Room({"right_door": "ST-9", "left_door":"ST-3", "go_back":"c_2"}, 
                             "\nYou step into a labratory filled with smashed control panels, analytics screens, and human-sized vats.", 
                             ["There's nothing intact to search."],
                             ""),
                "control_bridge": Room({"go_back":"c_3"}, 
                             "\nYou step onto the control deck. An epic battle of destiny awaits you. . . \n\n But it hasn't been written yet.",
                             "", True)
            }
        
        self.rooms['armory'].add_items(['blaster', 'pulse_rifle', 'phase_blade', 'stim'])
        self.rooms['ST-47'].add_items(['stim'])
        self.rooms['ST-3'].add_items(['stim'])
        self.rooms['ST-9'].add_items(['stim'])
        self.rooms['control_bridge'].add_items(['epic_salvage_of_destiny'])
        self.rooms['c_1'].add_entity(CharacterFactory('SPACE_PIRATE', 'Space-Pirate-1'))
        self.rooms['c_2'].add_entity(CharacterFactory('SPACE_PIRATE', 'Space-Pirate-2'))
        self.rooms['c_3'].add_entity(CharacterFactory('SPACE_PIRATE_CAPTAIN', 'Captain-Flare'))
        print()
        
        '''
        prompt user for character name
        '''
        # Opening Scene
        weapon_list = ['blaster', 'phase_blade', 'pulse_rifle', 'nothing']
        name = prompt(HTML("<ansigray>Kaydin: What's your name, kid?\n </ansigray>"), style=Style.from_dict({'': 'ansiyellow'}))
        self.player = CharacterFactory('PLAYER', name)
        dots()
        print(f"Kaydin: {name}, huh? This your first salvage run? You'll be a pile of goo if you go in like that. Grab something from the rack over there!")
        dots()
        weapon = next_action(weapon_list, 'Choose a weapon: ')
        dots()
        self.player.change_weapon(WeaponFactory(weapon))
        print("Kaydin: Nice choice! Now, let's get moving.")
        dots()
        
        opening_scene()

        alive = True
        self.current_room = "YV-4"
        print(self.rooms[self.current_room].text)
        
        while not self.salvage_found:
            if self.rooms[self.current_room].hasSpecial:
                print(self.rooms[self.current_room].special)
                self.rooms[self.current_room].set_hasSpecial(False)
                
            if self.rooms[self.current_room].entities:
                alive = combat(self.player, self.rooms[self.current_room])
                if not alive:
                    print('\nYou collapse to the deck, the world fading to darkness around you.')
                    dots()
                    print('\nGame Over')
                    break
                continue
            
            options = list(self.rooms[self.current_room].routes.keys())
            if self.rooms[self.current_room].hasCrate:
                options += ['open_chest']
            options += ['search']
            options += ['map']
            dots()
            action = next_action(options, "Choose an action: ")
            dots()
            
            if action == 'map':
                draw_map(self.current_room)
                
            if action == 'search':
                search_room(self.rooms[self.current_room].search)

            if action == 'open_chest':
                if len(self.rooms[self.current_room].items) == 0:
                    print('Chest is Empty')
                    time.sleep(1)
                else:
                    item = next_action(self.rooms[self.current_room].items, 'Choose an item to take: ')
                    if item == 'stim':
                        self.player.add_stim()
                        print('stim obtained!')
                    elif item == 'epic_salvage_of_destiny':
                        print('\n You have successfully obtained the Epic Salvage of Destiny!')
                        self.salvage_found = True
                    else:
                        self.player.change_weapon(WeaponFactory(item))
                        print(item + ' has been successfully equipped!')
                    self.rooms[self.current_room].remove_item(item)
                    
            if action in self.rooms[self.current_room].routes:
                self.current_room = self.rooms[self.current_room].routes[action]
                print(self.rooms[self.current_room].text)
            
        