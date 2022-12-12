import os;

if os.getcwd != "Task-1-Hapax":
    os.chdir("Task-1-Hapax")
    
def removePunctuations(string):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for letter in string:
        if letter in punctuations:
            string = string.replace(letter, "")
    return string


def returnHapaxes(filename):

    fileReader = open(filename, "r+")
    fileWriter = open("hapaxList.txt", "w")
    wordList = {}

    for lines in fileReader.readlines():
        words = lines.split()
        for word in words:
            word.lower()
            word = removePunctuations(word)
            wordList.setdefault(word)

    for words in wordList.keys():
        fileWriter.write(words + " ")

    fileReader.close()
    fileWriter.close()


def main():
    returnHapaxes("myTxt.txt")

if __name__ == "__main__":
    main()
