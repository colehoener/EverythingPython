from Base import Base

class ChildOne(Base):
    def __init__(self, guess):
        Base.__init__(self, "Printed Name!")
        self.guess = guess

    def printName(self):
        print(self.name)
        super().doSomething()