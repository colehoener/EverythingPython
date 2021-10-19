#Cole Hoener
#cth59
#Employee Class

class Employee():
    def __init__(self, employeeID, payRate = 0.0, numHours = 0.0):
        self.employeeID = employeeID
        self.numHours = float(numHours)
        self.payRate = float(payRate)
        self.grossWage = float(numHours) * float(payRate)

    #Setters

    def setNumHours(self, numHours):
        self.numHours = float(numHours)

    def setPayRate(self, payRate):
        self.payRate = float(payRate)

    #Getters 

    def getID(self):
        return self.employeeID

    def getNumHours(self):
        return self.numHours

    def getPayRate(self):
        return self.payRate

    def getGrossWage(self):
        self.grossWage = self.payRate * self.numHours
        return self.grossWage
    
    #Updates the gross wage in case there is some delay in function calls
    def updateGrossWage(self):
        self.grossWage = float(self.payRate) * float(self.numHours)

    def __str__(self):
        return ('Employee ID:  ' + str(self.employeeID)) + '\nHourly Rate:  ' + str(self.payRate) + '\nHours Worked: ' + str(self.numHours) + '\nGross Wages:  ' + str(self.grossWage) + '\n'