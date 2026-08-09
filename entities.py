class Player:
    def __init__(self, name):
        self.name = name
        
    def stats(self):
        return f"{self.rol} stats are: {self.health} HP and {self.attack_power} of damage"  

# Tank has more health but less attack power
class Tank(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 20
        self.rol = "Tank"
        
    
# Explorer receives less health
class Explorer(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.attack_power = 30
        self.rol = "Explorer"
        
# Soldier receives the same damage but makes more damage
class Soldier(Player):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 50        
        self.rol = "Soldier"
 
        
class Enemy:
    def __init__(self, name):
        self.name = name

    def stats(self):
        return f"You'll fight {self.rol} which stats are: {self.health} HP and {self.attack_power} of damage"  
        
# Demon it's the default soldier for enemies
class Demon(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 200
        self.attack_power = 50
        self.rol = "Demon"
        
# Beast works as a tank but for enemies
class Beast(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 15
        self.rol = "Beast"
    
# Witch is like the explorer but for enemies
class Witch(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 150
        self.attack_power = 30
        self.rol = "Witch"