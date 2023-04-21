class Inventory():
    def __init__(self, name, hero, description, damage, protection):
        self.name = name
        self.hero = hero
        self.description = description
        self.damage = damage
        self.protection = protection

    def __str__(self):
        summary = f"""
The {self.name} belongs to {self.hero} and has the following properties:
- {self.description}
Damage: {self.damage}
Protection: {self.protection}
        """
        return summary

