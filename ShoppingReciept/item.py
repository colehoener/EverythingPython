class item():
    def __init__(self, name = "None", price = 0, taxable = 1):
        self.__name = name
        self.__price = float(price)
        self.__taxable = taxable
        
    def __str__(self):
        price = float(self.__price)
        return (self.__name + str("_____________________________%.2f\n" %price))
    
    def getPrice(self):
        return float(self.__price)
    
    def getTax(self, tax):
        if (self.__taxable == 1):
            return self.__price * tax
        else:
            return 0