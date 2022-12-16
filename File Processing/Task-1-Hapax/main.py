import os;

if os.getcwd != "Task-1-Hapax": #to change directory to correct directory
    os.chdir("Task-1-Hapax")
    
def removePunctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for letter in string:
        if letter in punctuations:
            string = string.replace(letter, "") #replace punctuations with empty string
    return string

    
def returnHapaxes(filename):

    fileReader = open(filename, "r+")
    fileWriter = open("hapaxList.txt", "w")
    wordList = {} #use dict so i can store words as keys to remove duplicated automatically

    for lines in fileReader.readlines():
        words = lines.split()
        for word in words:
            word = word.lower()
            word = removePunctuations(word)
            wordList.setdefault(word) #append words to keys of wordList, if already exists then don't append

    for words in wordList.keys():
        fileWriter.write(words + " ") #write each key in wordList

    fileReader.close()
    fileWriter.close()
    print("Program finished")


def main():
    returnHapaxes("myTxt.txt")

if __name__ == "__main__":
    main()
