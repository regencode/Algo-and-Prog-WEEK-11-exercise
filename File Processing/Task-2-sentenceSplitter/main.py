import os

if os.getcwd != "Task-2-sentenceSplitter":
    os.chdir("Task-2-sentenceSplitter")

def checkEndOfSentence(word):
    ends = ".?!"
    exceptions = ["mr.", "mrs.", "dr.", "i.e.", "jr."]
    if word.lower() in exceptions:
        return False
    elif word[-1] in ends:
        return True
    else:
        return False

def sentenceSplitter(filename):
    fileReader = open(filename, "r")
    fileWriter = open("output.txt", "w")

    for lines in fileReader.readlines():
        words = lines.split()
        for word in words:
            fileWriter.write(word + " ")
            if checkEndOfSentence(word) == True:
                fileWriter.write("\n")
    
    fileReader.close()
    fileWriter.close()

def main():
    sentenceSplitter("myTxt.txt")


if __name__ == "__main__":
    main()
