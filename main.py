
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
            print(f"{self.name} of class{self.__class__.__name__ } is dead" )
            self.is_dead=True

        else: 
            print(f"{self.name} of class{self.__class__.__name__ } has {self.hp} hp left")
            

class Hero(Creature):
    def __init__(self, name, hp, attack_points):
        super().__init__(name, hp, attack_points)

    def heal(self):
        self.hp += 100
        if self.hp > 100:
            self.hp = 100
        self.checkHealth()

class Monster(Creature):
    def __init__(self, name, hp, attack_points, target):
        super().__init__(name, hp, attack_points)
        self.target = target

    def should_attack(self):
        if rd.randint(1,2) == 1 and self.is_dead == False:
            print("%s monster is attacking" %(self.name))
            self.attack(self.target)
        else:
            print("%s monster is not attacking" %(self.name))

    def attack(self, object_to_attack):
        object_to_attack.get_attacked(self.attack_points)

class NorskTeacher(Monster):
    def __init__(self,name, hp, attack_points, target):
        super().__init__(name, hp, attack_points, target)

    def supriseTest(self, object_to_attack):
        """
        The teacher has decided to test the class with a suprise test!
        50% chance of double damage if nynorsk test!
        """
        nynorsk_test=rd.randint(0,1)
        print(f"{self.name} used suprise test.")
        if nynorsk_test==1:
            print("And its nynorsk!!! Prepare to fail")
            object_to_attack.get_attacked(self.attack_points*2)    

    def spanishTube(self, object_to_attack):
        """
        You have been naughty
        Time for punishment! The teacher deals 1.2 times damage!
        """  
        print(f"{self.name} used spanish tube.")
        object_to_attack.get_attacked(self.attack_points*1.2)
    
    def nyNorskExam(self, object_to_attack):
        """
        You have your nynorsk exam tomorrow.
        Death is imminent
        """
        print(f"{self.name} used nynorsk exam. Say goodbye to your life")
        object_to_attack.get_attacked(self.attack_points*200)



    def attack(self, object_to_attack):
        attack_method=rd.randint(1,100)
        
        if attack_method<=10:
            self.supriseTest(object_to_attack)
        
        if attack_method<40 and attack_method>10:
            self.spanishTube(object_to_attack)

        if attack_method==100:
            self.nyNorskExam(object_to_attack)
            

if __name__== "__main__":
    hero_player = Hero("Knud Knudsen", 100, 20)

    ivar_monster = Monster("Ivar Aasen", 10, 50, hero_player)
    ingvild_teacher = NorskTeacher("Ingvild", 10, 10, hero_player)
    monster_list = [ivar_monster, ingvild_teacher]
    while True:
        print("\n")
        # Check if player is dead
        if hero_player.hp <= 0:
            print("Game over")
            exit()
        
        # Check all monsters are dead
        if not monster_list:
            print("You won!")
            exit()

        # Players turn
        while True:
            choice = input("Enter a for attack and h for heal: ")
            if choice == "a":
                # Choose random monster to attack
                monster_to_attack = rd.choice(monster_list)
                print("Player is attacking %s " %(monster_to_attack.name))
                # Attack monster
                hero_player.attack(monster_to_attack)
                break

            elif choice == "h":
                print("Player is healing")
                hero_player.heal()
                break
            else:
                print("Invalid input")

        # Monster attack
        items_to_remove = []
        for i in monster_list:
            if i.is_dead:
                print("%s is dead and will not attack" %(i.name))
                items_to_remove.append(i)
            else:
                i.should_attack()
        for i in items_to_remove:
            monster_list.remove(i)
        