#Cole Hoener
#cth59
#Node class
#Source: Prof. Medlock lecture notes

class Node():
    def __init__(self, data, next = None):
        self.__data = data 
        self.__next = next
    def getData(self): 
        return self.__data
    def getNext(self): 
        return self.__next
    def setData(self,d): 
        self.__data = d
    def setNext(self,n): 
        self.__next = n
    def __str__(self):
        return str(self.__data) + " whose next node is " + str(self.__next)