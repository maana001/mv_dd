
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
        self.checkHealth()

    def checkHealth(self):
        if self.hp==0:
            print(f"{self.name} of class{a.__class__.__name__ } is dead" )
        else: 
            print(f"{self.name} of class{a.__class__.__name__ } has {self.hp} hp left")
            

class Hero(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)
    

class Monster(Creature):
    def __init__(self, name, hp, attack_points):
        super.__init__(name, hp, attack_points)


class NorskTeacher(Monster):
    def __init__(self,name, hp, attack_points):
        super.__init__(name, hp, attack_points)

    def supriseTest(self):
        """
        The teacher has decided to test the class with a suprise test!
        50% chance of double damage if nynorsk test!
        """
        nynorsk_test=rd.randint(0,1)
        