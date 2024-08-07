from weapon import *
from random import randint
from helpers import *

def combat(p1, room: dict[str, Room]):
    # next_action
    dots()
    for e in room.get_entities().copy():
        print('You see an enemy before you! Yikes!')
        dots()
        ene = room.get_entities()[e]
        while ene.hp > 0:
            print('HP: ' + str(p1.hp))
            print('ENEMY HP: ' + str(ene.hp))
            if player_goes_first(p1, ene):
                player_turn(p1, ene)
                if ene.hp <= 0:
                    room.remove_entity(ene)
                    continue
                enemy_turn(p1, ene)
                if p1.hp <= 0:
                    return False
            else:
                enemy_turn(p1, ene)
                if p1.hp <= 0:
                    return False
                player_turn(p1, ene)
                if ene.hp <= 0:
                    room.remove_entity(ene)
                    continue
    print('Your pierce your enemy\'s shields and they flail backwards, their body drifting away. You have vanquished your foe.')
    return True


def enemyList(entities):
    enemies = []  
    for e in entities:
        enemies.append(e)
    return enemies  

def player_goes_first(p1, e):   
    if p1.weapon.speed >= e.weapon.speed:
        return True
    else:
        return False
    
def player_turn(p1, e):
    options = ['attack']
    if p1.stim > 0:
        options.append('use_stim')
    choice = next_action(options, "Which action would you like to perform: ")
    dots()
    
    if choice == 'attack':
        print('You attempt an attack.')
        dots()
        dmg = p1.weapon.damage
        roll = randint(1, 20)
        hit_chance = roll * p1.weapon.accuracy
        
        if roll >= 19:
            dmg *= 2
            e.hp -= dmg
            print(p1.weapon.crit_txt)
        elif hit_chance >= 50:
            e.hp -= dmg
            print(p1.weapon.hit_txt)
        else:
            print(p1.weapon.miss_txt)
    if choice == 'use_stim':
        print('You feel a cooling sensation as the stim takes effect.')
        p1.use_stim()
    dots()
    
def enemy_turn(p, e):
    print(e.name + ' attempts an attack.')
    dots()
    dmg = e.weapon.damage
    roll = randint(1, 20)
    hit_chance = roll * e.weapon.accuracy
    
    if p.weapon.close_proximity:
        hit_chance *=2
    if roll >= 19:
        dmg *= 2
        p.hp -= dmg
        print(e.weapon.crit_txt)
    elif hit_chance >= 50:
        p.hp -= dmg
        print(e.weapon.hit_txt)
    else:
        print(e.weapon.miss_txt)
    dots()