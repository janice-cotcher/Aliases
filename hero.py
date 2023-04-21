from inventory import Inventory


class Hero(object):
    def __init__(self, name, power, identity):
        self.name = name
        self.power = power
        self.identity = identity

    def say_hello(self):
        print('Hello, evil-doers! My name is', self.name + '!')
        print('My super power is', self.power, 'so you better beware.')

    def divulge(self):
        print('My real name is', self.identity)


class Vehicle():
    def __init__(self, name, hero, protection, attack):
        self.name = name
        self.hero = hero
        self.protection = protection
        self.attack = attack

    def __str__(self):
        description = f"""
The {self.name} can only be used by {self.hero}.
The {self.name} has a protection value of {self.protection}.
The {self.name} has an attack value of {self.attack}
        """
        return description



def print_items(list):
    for item in list:
        print(item)
        print("\n")



lasso = Inventory("Lasso of Truth", "Wonder Woman", "extracts truth from people", 0, 5)
bracelet = Inventory("Bracelets of Submission", "Wonder Woman", "bulletproof bracelets", 100, 50)
sword = Inventory("Sword of Athena", "Wonder Woman", "magically-empowered sword wielded", 500, 0)
batarang = Inventory("Batarang", "Batman", "boomerang shaped like a bat", 10, 0)
grapple = Inventory("Grappling Hook", "Batman", "spear-shooting spring-based device", 5, 0)
sonic = Inventory("Sonic Bat Device", "Batman", "high frequency emitter allowing the control of bats", 15, 100)
items = [lasso, bracelet, sword, batarang, grapple, sonic]


                     
