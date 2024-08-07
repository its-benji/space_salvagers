class Weapon:
    def __init__(self, name, description, damage, speed, accuracy, close_proximity, hit_txt, crit_txt, miss_txt):
        self.name = name
        self.description = description
        self.damage = damage
        self.speed = speed
        self.accuracy = accuracy
        self.close_proximity = close_proximity
        self.hit_txt = hit_txt
        self.crit_txt = crit_txt
        self.miss_txt = miss_txt

def WeaponFactory(weapon_type):
    '''
    insert your weapons here
    '''
    if weapon_type == 'blaster':
        return Weapon(weapon_type, 'An old blaster', 25, 5, 7, False, 'The blaster shot hits its target.', 'The blaster shot inflicts CRITICAL damage.', 'The blaster shot narrowly misses.')
    elif weapon_type == 'phase_blade':
        return Weapon(weapon_type, 'Not A Lightsaber', 40, 1, 7, True, 'Your phase-blade connects with its target.', 'The phase-blade arcs through the air in a powerful strike. CRITICAL damage.', 'The blade swings wide, narrowly missing its target.')
    elif weapon_type == 'pulse_rifle':
        return Weapon(weapon_type, 'More powerful than the blaster, but a bit slower', 35, 4, 5, False, 'The pulse-rifle hits its target!', 'The pulse-rifle shot inflicts CRITICAL damage.', 'The pulse-rifle shot narrowly misses.')
    elif weapon_type == 'nothing':
        return Weapon(weapon_type, 'Been nice knowin\' ya kid', 5, 2, 8, True, 'You slam your fist into the target - it\'s not very effective.', 'Bruce Lee who? CRITICAL damage!', 'You swing wildly and miss your target.')
    else:
        print('error invalid weapon type')
