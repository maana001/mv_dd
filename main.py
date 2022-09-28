
import random as rd

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
        super().__init__(name, hp, attack_points)
    

class Monster(Creature):
    def __init__(self, name, hp, attack_points, target):
        super().__init__(name, hp, attack_points)
        self.target = target

    def should_attack(self):
        if rd.randint(1,10) == 5:
            self.attack(self.target)



# knud_knudsen.attack(ivar_aasen)
# ivar_aasen.giveInfo()

# ivar_aasen.attack(knud_knudsen)
# knud_knudsen.giveInfo()

if __name__== "__main__":
    knud_knudsen = Hero("Knud", 100, 20)

    ivar_aasen = Monster("Ivar", 100, 90, knud_knudsen)
    monster_list = [ivar_aasen]
    while True:
        for i in monster_list:
            i.should_attack()

