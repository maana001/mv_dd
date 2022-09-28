
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
            print(f"{self.name} of class{self.__class__.__name__ } is dead" )
        else: 
            print(f"{self.name} of class{self.__class__.__name__ } has {self.hp} hp left")
            

class Hero(Creature):
    def __init__(self, name, hp, attack_points):
        super().__init__(name, hp, attack_points)

    def heal(self):
        self.hp += 20
        if self.hp > 100:
            self.hp = 100

class Monster(Creature):
    def __init__(self, name, hp, attack_points, target):
        super().__init__(name, hp, attack_points)
        self.target = target

    def should_attack(self):
        if rd.randint(1,10) == 5:
            self.attack(self.target)

class NorskTeacher(Monster):
    def __init__(self,name, hp, attack_points):
        super.__init__(name, hp, attack_points)

    def supriseTest(self):
        """
        The teacher has decided to test the class with a suprise test!
        50% chance of double damage if nynorsk test!
        """
        nynorsk_test=rd.randint(0,1)
        
if __name__== "__main__":
    hero_player = Hero("Knud Knudsen", 100, 20)

    ivar_monster = Monster("Ivar Aasen", 100, 50, hero_player)
    ingvild_teacher = NorskTeacher("Ingvild", 100, 10)
    monster_list = [ivar_monster, ingvild_teacher]
    while True:
        # Check if player is dead
        if hero_player.hp <= 0:
            print("Game over")
            exit()
        
        # Players turn
        while True:
            choice = input("Enter a for attack and h for heal: ")
            if choice == "a":
                hero_player.attack(monster_list[0])
                break
            elif choice == "h":
                hero_player.heal()
                break
            else:
                print("Invalid input")

        # Monster attack
        for i in monster_list:
            if i.is_dead:
                print("%s is dead and will not attack" %(i.name))
            else:
                i.should_attack()

        