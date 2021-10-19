from monster import monster

class urmom(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 25

    def __str__(self): #The real monster. 
        return "I am your mom, " + self.__name

    def getName(self): #Name of your mom. 
        return self.__name

    def getDescription(self): #Accurate description of my mom.
        return "Your mom is angry, tired, and telling you to clean your room."
    
    def basicAttack(self,enemy): #Basic attack
        enemy.doDamage(3)

    def basicName(self): #Intimidating basic attack name
        return "Slap"

    def defenseAttack(self,enemy): #Mom be careful. 
        enemy.doDamage(3)
        self.doDamage(-2)

    def defenseName(self): #Most powerful mom defense. 
        return "Ignore"

    def specialAttack(self,enemy):
        enemy.doDamage(6)

    def specialName(self):
        return "I'm so dissapointed in you"

    def getHealth(self):
        return self.__health

    def doDamage(self,damage):
        self.__health = self.__health - damage
            
    def resetHealth(self):
        self.__health = 25