from monster import monster

class depression(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 25

    def __str__(self): 
        return "I am depression, " + self.__name

    def getName(self): 
        return self.__name

    def getDescription(self): 
        return "A plastic bag takes 1000 years to break down. You only take one night. Depression."
    
    def basicAttack(self,enemy): 
        enemy.doDamage(3)

    def basicName(self): 
        return "CS172"

    def defenseAttack(self,enemy): 
        enemy.doDamage(3)
        self.doDamage(-2)

    def defenseName(self): 
        return "Dopamine"

    def specialAttack(self,enemy):
        enemy.doDamage(6)

    def specialName(self):
        return "Let's take this Seratonin and dump it down the drain."

    def getHealth(self):
        return self.__health

    def doDamage(self,damage):
        self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 25