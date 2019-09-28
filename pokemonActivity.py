class Pokemon:
    count = 0
    def __init__(self, name, hp, element, level, exp):
        self.name = name
        self.hp = hp
        self.element = element
        self.level = level
        self.exp = exp
        Pokemon.count += 1
    
    def levelUp(self):
        self.level += 1

charizard = Pokemon("Charizard", 180, "fire", 5, 0)
print(charizard.element)
charizard.levelUp()
print(charizard.level)
