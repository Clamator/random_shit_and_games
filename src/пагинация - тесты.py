class Character:
    def __init__(self, armor=50, attack=50):
        self.armor = armor
        self.attack = attack
        self.health = 50

    def heal(self):
        if self.health >= 100:
            self.health = 100
            return self
        self.health += 30
        return self

    def damage(self):
        self.health -= 20
        return self


