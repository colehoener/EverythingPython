from monster import monster

class kraken(monster):
    def __init__(self, name):
        self.__name = name
        self.__health = 25
        self.__basicName = "Bite"
        self.__description = "The mighty squid of the sea!"
        self.__defenseName = "Dive"
        self.__specialName = "Tentacle Whip"
    
    def getName(self):
        return self.__name
    
    def getDescription(self):
        return self.__description

    def basicAttack(self,enemy):
        enemy.doDamage(2)

    def basicName(self):
        return (self.__basicName)

    def defenseAttack(self,enemy):
        enemy.doDamage(1)
        self.doDamage(-2)

    def defenseName(self):
        return(self.__defenseName)

    def specialAttack(self,enemy):
        enemy.doDamage(7)

    def specialName(self):
        return(self.__specialName)

    def getHealth(self):
        return(self.__health)

    def doDamage(self,damage):
        self.__health = self.__health - damage

    def resetHealth(self):
        self.__health = 25

