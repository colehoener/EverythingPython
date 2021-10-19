#Cole Hoener
#cth59
#Main script for HW5 (Payroll program)

from linkedList import LinkedList
from node import Node
from employee import Employee

employeeList = LinkedList()

choice = 'a'

#Main loop of program
while choice != 'f':
    print('\n*** CS 172 Payroll Simulator ***')
    print("a. Add New Employee")
    print("b. Calculate Weekly Wages")
    print("c. Display Payroll")
    print("d. Update Employee Hourly Rate")
    print("e. Remove Employee from Payroll")
    print("f. Exit the program\n")

    choice = input("Enter your choice: ")

    if(choice == 'a'):
        #Choice A: (Enter new employee)
        ID = input("Enter the new employee ID: ")
        rate = input("Enter the hourly rate:  ")
        newEmployee = Employee(ID, rate)
        employeeList.append(Node(newEmployee))
    elif(choice == 'b'):
        #Choice B: (Enter num hours worked)
        for i in range(employeeList.__len__()):
            hours = input("Enter hours worked for employee " + str((employeeList.__getitem__(i)).getData().getID()) + " : ")
            (employeeList.__getitem__(i)).getData().setNumHours(hours)
    elif(choice == 'c'):
        #Choice C: (Prints payroll)
        print("\n *** Payroll ***")
        for i in range(employeeList.__len__()):
            (employeeList.__getitem__(i)).getData().updateGrossWage()
            print((employeeList.__getitem__(i)).getData())
        print()
    elif(choice == 'd'):
        #Choice D: (Updates employee hourly rate)
        ID = input("Enter ID of employee: ")
        for i in range(employeeList.__len__()):
            if (employeeList.__getitem__(i)).getData().getID() == ID:
                rate = input("Enter new hourly rate:  ")
                (employeeList.__getitem__(i)).getData().setPayRate(rate)
    elif(choice == 'e'):
        #choice E: (Removes emploee from the list)
        ID = input("Enter the ID of the employee to remove from payroll: ")

        for i in range(employeeList.__len__()):
            if (employeeList.__getitem__(i)).getData().getID() == ID:
                index = employeeList.__getitem__(i)
        employeeList.remove(index)

        print("Done.\n")
    elif(choice == 'f'):
        #choice F: (Exits code)
        print("Good-Bye!")
        exit()
    else:
        print("Invaild choice. Try again.")