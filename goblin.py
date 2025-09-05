import random
from enemy import Enemy 


class Goblin:
    """
    This is our goblin blueprint 
    
    Attributes:
        name: Awe, it has a name? How cute!
        health: The current health value 
        attack_power: How much health will be drained from opponent if hit
    """
    class Goblin(Enemy): 
        def __init__(self, name, color):
            super()._init__(name)
            self.color = color


