class Weapon:
    def __init__(self, name, description, damage, speed, accuracy, ammo):
        self.name = name
        self.description = description
        self.damage = damage
        self.speed = speed
        self.accuracy = accuracy
        self.ammo = ammo

def WeaponFactory(weapon_type):
    '''
    insert your weapons here
    '''
    if weapon_type == 'BLASTER':
        return Weapon(weapon_type, 'An old blaster', 25, 1.0, 0.7, 24)
    elif weapon_type == 'PHASE_BLADE':
        return Weapon(weapon_type, 'Not A Lightsaber', 50, 5.0, 0.9, 999)
    elif weapon_type == 'PULSE_RIFLE':
        return Weapon(weapon_type, 'More powerful than the blaster, but a bit slower', 35, 3.0, 0.6, 16)
    elif weapon_type == 'NOTHING':
        return Weapon(weapon_type, 'Been nice knowin\' ya kid', 5, 4.0, 0.8, 999)
    else:
        print('error invalid weapon type')
