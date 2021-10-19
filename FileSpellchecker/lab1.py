from spellchecker import spellchecker

def get_file():
        fileText = input("Enter File Name: ")
        try:
            f = open(fileText)
            return f
        except FileNotFoundError:
            print("File not found {}".format(fileText))
            return get_file()

lineCount = 1
wordsRight = 0
wordsWrong = 0
totalWords = 0

SP = spellchecker("english_words.txt")

print("Welcome to Text File Spellchecker.")

fileText = get_file()

for lines in fileText.readlines():
    for word in lines.split():
        if(SP.check(word)):
            wordsRight += 1
        else:
            print("Possible Spelling Error on line", lineCount, ":", word)
            wordsWrong += 1
        totalWords += 1
    lineCount += 1

print('{:,.0f}'.format(wordsRight), "words passed spell checker.")
print('{:,.0f}'.format(wordsWrong), "word failed spell checker.")
percentage = (wordsRight / totalWords * 100)
print("%0.2f%% of the words passed." %percentage)



