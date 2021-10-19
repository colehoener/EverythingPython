from item import item 

class receipt():
    def __init__(self, tax_rate = 0.07):
        self.__tax_rate = tax_rate
        self.__purchases = []

    def __str__(self):
        output = ""
        totalTax = 0.0
        subTotal = 0.0

        for i in range(len(self.__purchases)):
            output = output + str(self.__purchases[i])
            totalTax = totalTax + self.__purchases[i].getTax(0.07)
            subTotal = subTotal + self.__purchases[i].getPrice()
        
        output = output + ("\nSub Total___________________________{:.2f}\n".format(subTotal))
        output = output + ("Tax_________________________________{:.2f}\n".format(totalTax))
        output = output + ("Total_______________________________{:.2f}\n".format(subTotal + totalTax))

        return output
    
    def addItem(self, newItem = item()):
        self.__purchases.append(newItem)


