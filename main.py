
import random as rd

class Creature:
    def __init__(self,name, hp,attack_points):
        self.name=name
        self.hp=hp
        self.attack_points=attack_points
        self.is_dead=False

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
        if self.hp<=0:
            print(f"{self.name} of class{a.__class__.__name__ } is dead" )
            isDead=True
            
        else: 
            print(f"{self.name} of class{a.__class__.__name__ } has {self.hp} hp left")
            

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

    def attack(self, object_to_attack):
        if self.is_dead==False:
           object_to_attack.get_attacked(self.attack_points)

class NorskTeacher(Monster):
    def __init__(self,name, hp, attack_points):
        super.__init__(name, hp, attack_points)

    def supriseTest(self):
        """
        The teacher has decided to test the class with a suprise test!
        50% chance of double damage if nynorsk test!
        """
        nynorsk_test=rd.randint(0,1)
        if nynorsk_test==1:
            self.attack_points=self.attack_points*2
    

    def spanishTube(self):
        """
        You have been naughty
        Time for punishment! The teacher deals 1.2 times damage!
        """  
        self.attack_points=self.attack_points*1.2
    
    def nyNorskExam(self):
        """
        You have your nynorsk exam tomorrow.
        This means instant death
        """
        self.attack_points=1000

    def attack(self, object_to_attack):
        attack_method=rd.randint(1,100)
        if attack_method<=10:
            self.supriseTest()
        if attack_method<40 and attack_method>10:
            self.spanishTube()
        if attack_method==100:
            self.nyNorskExam()
            
        if self.is_dead==False:
           object_to_attack.get_attacked(self.attack_points)


        
if __name__== "__main__":
    knud_knudsen = Hero("Knud", 100, 20)

    ivar_aasen = Monster("Ivar", 100, 90, knud_knudsen)
    monster_list = [ivar_aasen]
    while True:
        for i in monster_list:
            i.should_attack()