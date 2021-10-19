from maze import Maze
from room import Room

my_rooms = []
my_rooms.append(Room("This room is the entrance."))
my_rooms.append(Room("This room has a table. Maybe a dinning room?"))
my_rooms.append(Room("This is your brothers room."))
my_rooms.append(Room("This is a bathroom."))
my_rooms.append(Room("You can't see a thing in this room!"))
my_rooms.append(Room("Is this Narnia?"))
my_rooms.append(Room("Welcome to Hogwarts."))
my_rooms.append(Room("You don't want to know what is happening in this room"))
my_rooms.append(Room("Kobe? Is that you?"))
my_rooms.append(Room("you found the exit!"))

#Solution: Go north, north, north, north, east, north

#room 0 is south of room 1
my_rooms[0].setNorth(my_rooms[1])
my_rooms[1].setSouth(my_rooms[0])
#Room 2 is east of room 1
my_rooms[1].setEast(my_rooms[2])
my_rooms[2].setWest(my_rooms[1])
#Room 3 is north of  room 1
my_rooms[1].setNorth(my_rooms[3])
my_rooms[3].setSouth(my_rooms[1])
#Room 4 is west of room 3
my_rooms[3].setWest(my_rooms[4])
my_rooms[4].setEast(my_rooms[3])
#Room 5 is north of room 4
my_rooms[5].setSouth(my_rooms[4])
my_rooms[4].setNorth(my_rooms[5])
#Room 6 is north of room 3
my_rooms[6].setSouth(my_rooms[3])
my_rooms[3].setNorth(my_rooms[6])
#Room 6 is east of room 5
my_rooms[6].setWest(my_rooms[5])
my_rooms[5].setEast(my_rooms[6])
#Room 7 is north  of room 6
my_rooms[7].setSouth(my_rooms[6])
my_rooms[6].setNorth(my_rooms[7])
#Room 8 is west of room 7
my_rooms[8].setWest(my_rooms[7])
my_rooms[7].setEast(my_rooms[8])
#Room 9 is north of roomn 8
my_rooms[9].setSouth(my_rooms[8])
my_rooms[8].setNorth(my_rooms[9])

my_maze = Maze(my_rooms[0],my_rooms[9])

while(my_maze.atExit() != True):
    print(my_maze.getCurrent())

    direction = input("Enter direction to move, north, west, east, south, or reset\n")

    if(direction == "north"):
        if(my_maze.getCurrent().getNorth()):
            my_maze.moveNorth()
            print("You went north")
        else:
            print("Direction invalid, try again.")
    elif(direction == "west"):
        if(my_maze.getCurrent().getWest()):
            my_maze.moveWest()
            print("You went west")
        else:
            print("Direction invalid, try again.")
    elif(direction == "east"):
        if(my_maze.getCurrent().getEast()):
            my_maze.moveEast()
            print("You went east")
        else:
            print("Direction invalid, try again.")
    elif(direction == "south"):
        if(my_maze.getCurrent().getSouth()):
            my_maze.moveSouth()
            print("You went south")
        else:
            print("Direction invalid, try again.")
    elif(direction == "reset"):
        my_maze.reset()
        print("You went back to the start!")
    else:
        print("Invaild input, try again")
    
    if(my_maze.atExit()):
        print("You found the exit!")