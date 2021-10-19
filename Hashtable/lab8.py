from Birthday import Birthday

hashTable = []
i = 0
fileText = 'bdaylist.txt'

for i in range(12):
    hashTable.append([])

#opens file
try:
    f = open(fileText)
except FileNotFoundError:
    print("File not found {}".format(fileText))

#reads lines from file and creates Birthday objects
for lines in f.readlines():
    #read
    birthday = lines.split('/')
    month = int(birthday[0])
    day = int(birthday[1])
    year = int(birthday[2])

    #add to hash table
    bday = Birthday(month,day,year)

    hashTable[hash(bday)].append((Birthday(month,day,year), i))
    i += 1
    
i = 0
for j in hashTable:
    print("Hash location", i, "has", len(j), "elements in it")
    i += 1


