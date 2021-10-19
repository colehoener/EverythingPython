from Base import Base

class ChildOne(Base):
    def __init__(self, guess):
        self.guess = guess

    def printName(self):
        print(self.name)