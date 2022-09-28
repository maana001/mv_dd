
class Creature:
    def __init__(self,name, hp,attackPoints):
        self.name=name
        self.hp=hp
        self.attackPoints=attackPoints

    def attack(self, object_to_attack):
        object_to_attack.get_attacked(self.attack_points)
    
    def get_attacked(self, hp_reduce):
        self.hp -= hp_reduce

class Hero(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)
    

class Monster(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)