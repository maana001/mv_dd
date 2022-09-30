
import random as rd

class Creature:
    def __init__(self,name, hp,attack_points):
        # Name of character displayed in messages
        # printed in terminal
        self.name=name
        # Health points
        self.hp=hp
        # Default damage dealt to other creatures
        # when attacking
        self.attack_points=attack_points
        # Boolean for checking if creature has hp > 0
        self.is_dead=False

    def giveInfo(self):
        print("###################")
        print("This is my life story")
        print("hp: ", self.hp)
        print("name: ", self.name)
        print("attackPoints:", self.attack_points)
        print("###################")

    def attack(self, object_to_attack):
        # Attack object
        object_to_attack.get_attacked(self.attack_points)
    
    def get_attacked(self, hp_reduce):
        # Reduce hp
        self.hp -= hp_reduce
        self.checkHealth()

    def checkHealth(self):
        """ Checks if creature is dead. Prints this to terminal. If not 
        it's healthpoints are printed to terminal """
        # Check if creature is alive
        if self.hp <= 0:
            print(f"{self.__class__.__name__ } {self.name} is dead" )
            self.is_dead=True
        else: 
            print(f"{self.__class__.__name__ } {self.name}  has {self.hp} hp left")

class Hero(Creature):
    """ Main player """
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
        if nynorsk_test==1:
            object_to_attack.get_attacked(self.attack_points*2)    

    def spanishTube(self, object_to_attack):
        """
        You have been naughty
        Time for punishment! The teacher deals 1.2 times damage!
        """  
        object_to_attack.get_attacked(self.attack_points*1.2)
    
    def nyNorskExam(self, object_to_attack):
        """
        You have your nynorsk exam tomorrow.
        This means instant death
        """
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

    # Create a hero (player)
    hero_player = Hero("Knud Knudsen", 100, 20)
    # Create monsters
    ivar_monster = Monster("Ivar Aasen", 100, 50, hero_player)
    ingvild_teacher = NorskTeacher("Ingvild", 100, 10, hero_player)
    # List containing monsters that can attack the hero
    monster_list = [ivar_monster, ingvild_teacher]

    while True:
        print()

        # Check if player is dead
        if hero_player.hp <= 0:
            print("Game over")
            exit()
        
        # Check if all monsters are dead
        if not monster_list:
            print("You won!")
            exit()

        # Players turn, repeat until valid input
        while True:
            choice = input("Enter a for attack and h for heal: ")
            # Attack monster
            if choice == "a":
                # Choose random monster to attack
                monster_to_attack = rd.choice(monster_list)
                print("Player is attacking %s " %(monster_to_attack.name))
                # Attack monster
                hero_player.attack(monster_to_attack)
                break
            # Heal player
            elif choice == "h":
                print("Player is healing")
                hero_player.heal()
                break
            # Input is invalid, ask user to give valid input
            else:
                print("Invalid input")

        # If the monster gets killed it is added to this list
        # and removed from the gameplay
        items_to_remove = []
        # Monsters turn to attack
        for i in monster_list:
            # Check if monster is dead or not
            if i.is_dead:
                print("%s is dead and will not attack anymore" %(i.name))
                items_to_remove.append(i)
            else:
                # Check if the monster should attack
                i.should_attack()
        # Remove dead monsters from the gameplay
        for i in items_to_remove:
            monster_list.remove(i)
        