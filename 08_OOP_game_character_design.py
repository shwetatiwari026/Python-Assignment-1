class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        print(f"{self.name} has {self.health} health points.")

    def attack(self):
        print(f"{self.name} performs a basic attack.")


class Warrior(Character):
    def attack(self):
        print(f"{self.name} swings a sword.")


class Healer(Character):
    def attack(self):
        print(f"{self.name} uses a healing ability.")


class Archer(Character):
    def attack(self):
        print(f"{self.name} shoots an arrow.")


characters = [
    Warrior("Arjun", 100),
    Healer("Mira", 80),
    Archer("Ravi", 90)
]

for character in characters:
    character.introduce()
    character.attack()
