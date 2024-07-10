from weapon import WeaponFactory

class Character:
    def __init__(self, name, hp, weapon, stim=0):
        self.name = name
        self.hp = hp
        self.weapon = weapon
        self.stim = stim

    def change_weapon(self, weapon):
        self.weapon = weapon
    
    def add_stim(self):
        self.stim += 1
    
    def use_stim(self):
        if self.stim >= 1:
            self.hp += 50
            self.stim -= 1

def CharacterFactory(char_type, name):
    if char_type == 'PLAYER':
        return Character(name, 200, WeaponFactory('NOTHING'))
    elif char_type == 'SPACE_PIRATE':
        return Character('Pirate', 100, WeaponFactory('PULSE_RIFLE'))
    else:
        print('error, invalid character type')

