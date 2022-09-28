
class Creature:
    def __init__(self,name, hp,attack_points):
        self.name=name
        self.hp=hp
        self.attack_points=attack_points

    def giveInfo(self):
        print("###################")
        print("This is my life story")
        print("hp: ", self.hp)
        print("name: ", self.name)
        print("attackPoints:", self.attack_points)
        print("###################")

    def attack(self, object_to_attack):
        object_to_attack.get_attacked(self.attack_points)
    
    def get_attacked(self, hp_reduce):
        self.hp -= hp_reduce

class Hero(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)
    

class Monster(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)checkHealth(self):
        if self.hp==0:
            print()