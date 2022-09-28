
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

    def checkHealth(self):
        if self.hp==0:
            print()