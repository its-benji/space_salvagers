class Room:
    def __init__(self, routes: list[str], text, search: list[str], special: str, hasCrate=False, hasSpecial=False):
        self.entities = {}
        self.items = []
        self.weapons = []
        self.hasCrate = hasCrate
        self.text = text
        self.routes = routes
        self.search = search
        self.special = special
        self.hasSpecial = hasSpecial

    def add_entity(self, entity):
        self.entities[entity.name] = entity
        
    def get_entities(self):
        return self.entities
        
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
        
    def set_hasSpecial(self, boo):
        self.hasSpecial = boo