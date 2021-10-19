from monster import monster

class medlock(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 20
        self.__basicName = "Zybooks home work"
        self.__description = "The best programming profffesor at Drexel University!"
        self.__defenseName = "\"I'll fix that later\""
        self.__specialName = "Kahoot for attendence"
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description

    def basicAttack(self,enemy):
        enemy.doDamage(5)

    def basicName(self):
        return (self.__basicName)

    def defenseAttack(self,enemy):
        enemy.doDamage(3)
        self.doDamage(-1)

    def defenseName(self):
        return(self.__defenseName)

    def specialAttack(self,enemy):
        enemy.doDamage(6)

    def specialName(self):
        return(self.__specialName)

    def getHealth(self):
        return(self.__health)

    def doDamage(self,damage):
        self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 20