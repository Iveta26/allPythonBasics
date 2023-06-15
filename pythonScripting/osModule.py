
# Using OS to do things

import os

# echo to the terminal
os.system('echo "Hello World!"')

# make and change directories

directory = "testDir"

parentDir = "C:/Users/iveta_6esu9b1/PycharmProjects"

path = os.path.join(parentDir, directory)

# os.mkdir(path) #making dir


# put a file into dir we just made

fileName = "testFile.txt"
filePath = os.path.join(path, fileName)


with open(filePath, "w") as file1:
    toFile = "Contents of file are written here"
    file1.write(toFile)