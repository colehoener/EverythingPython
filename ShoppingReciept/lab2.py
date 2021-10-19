from receipt import receipt
from item import item
import datetime

doAgain = "yes"
shoppingReciept = receipt(0.07)

print("Welcome to Receipt Creator")

while(doAgain == "yes" or doAgain == "Yes"):
    itemName = input("Enter item name: ")
    itemPrice = input("Enter item price: ")
    isTaxable = input("Is the item taxable (yes/no): ")
    doAgain = input("Add another item (yes/no): ")

    if(isTaxable == "yes"):
        newItem = item(itemName, itemPrice, 1)
    else:
        newItem = item(itemName, itemPrice, 0)

    shoppingReciept.addItem(newItem)


timeStamp = str(datetime.datetime.now())

print("----- " + timeStamp + " -----")
print(shoppingReciept)


    
        