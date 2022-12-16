import os

if os.getcwd != "Task-2-sentenceSplitter":
    os.chdir("Task-2-sentenceSplitter")

def checkEndOfSentence(word):
    ends = ".?!"
    exceptions = ["mr.", "mrs.", "dr.", "i.e.", "jr."] #titles so they are not end of sentence
    if word.lower() in exceptions:
        return False
    elif word[-1] in ends: #if end of word is any of the punctuations that marks the end of a sentence, return True
        return True
    else:
        return False

def sentenceSplitter(filename):
    fileReader = open(filename, "r")
    fileWriter = open("output.txt", "w")

    for lines in fileReader.readlines(): #read each line
        words = lines.split()  #turn line into list of words
        for word in words:
            fileWriter.write(word + " ") #write to output
            if checkEndOfSentence(word) == True: #if word marks end of sentence, add newline character
                fileWriter.write("\n")
    
    fileReader.close()
    fileWriter.close()

def main():
    sentenceSplitter("myTxt.txt")


if __name__ == "__main__":
    main()
