import hero as h


def hero_vehicle(vehicles):
    """print a list of the hero's vehicles"""
    for vehicle in vehicles:
        print(vehicle)



bruce = h.Hero('Batman', 'martial arts', 'Bruce Wayne')
bruce.say_hello()
bruce.divulge()
print("\n")
diana = h.Hero('Wonder Woman', 'super strength', 'Diana Prince')
diana.say_hello()
diana.identity = "changed!"
diana.divulge()
print("\n")

# define hero's vehicles and characteristics
invisiblePlane = h.Vehicle("Invisible Plane", "Wonder Woman", 100, 20)
tumbler = h.Vehicle("Tumbler", "Batman", 100, 50)
batmobile = h.Vehicle("Batmobile", "Batman", 100, 50)
bat = h.Vehicle("Bat", "Batman", 0, 20)
batpod = h.Vehicle("Batpod", "Batman", 50, 50)

vehicles = [invisiblePlane, tumbler, batmobile, bat, batpod]
hero_vehicle(vehicles)
h.print_items(h.items)


