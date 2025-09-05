import random
from enemy import Enemy 


class boss_baby(Enemy):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        # Boss has more health and power
        self.health = 350
        self.attack_power = 23

    def attack(self): 
        if self.health < 10: 
            self.attack_power = self.health * 5
            print("Big Boss is MAAAAAAAAD!!!!!!!!!")
        

        return self.attack_power
