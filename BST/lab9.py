import random
import time
import matplotlib.pyplot as plt
from BST import BST

def populate(n):
    array = []
    tree = BST()
    
    for i in range(n - 1):
        randNum = random.randint(0,n+1)
        array.append(randNum)
        tree.append(randNum)

    array.append(5)
    tree.append(5)
    

    return (array, tree)

def search(array, k):
    for i in array:
        if i == k:
            return True
    return False

n = 10000

myList, myTree = populate(n)

#Searches list
timeB4 = time.time()
if(search(myList, 5)):
    timeAfter = time.time()
    print ((timeAfter - timeB4) * 1000000, "ns")
else:
    print("Number not found")

#Searches tree binary
timeB4 = time.time()
if(myTree.isin(5)):
    timeAfter = time.time()
    print ((timeAfter - timeB4) * 1000000, "ns")
else:
    print("Number not found")


n = 0

averageList = 0
averageTree = 0
aList = []
aTree = []
nList = []

while n < 10000:
    if(n % 100 == 0):
        myList, myTree = populate(n)

    #Searches list
    timeB4 = time.time()
    if(search(myList, 5)):
        timeAfter = time.time()
        averageList += (timeAfter - timeB4)
        if(n % 1000 == 0 and n != 0):
            aList.append((averageList / n) * 10.0)


        #Searches tree binary
    timeB4 = time.time()
    if(myTree.isin(5)):
        timeAfter = time.time()
        averageTree =+ (timeAfter - timeB4)
        if(n % 1000 == 0 and n != 0):
            aTree.append((averageTree / n) * 10.0)
    

    if(n % 1000 == 0 and n != 0):
        nList.append(n)
    
    n+=1

print(aTree)
plt.plot((nList),(aList),label='List (ns)')
plt.plot((nList),(aTree),label='Binary Tree (ns)')

plt.legend()
plt.show()