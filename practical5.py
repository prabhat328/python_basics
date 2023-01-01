# Practical 5


# creating a file and writing in it
writing = open("new_writing.txt", 'w')
writing.write("Created a new file to write something")
writing.write("\nPrabhat Tiwari, KFBSC(IT)079")
writing.close()

# opening a file to read
rea = open("reading.txt", 'r')
print("file name =", rea.name)
print("mode =", rea.mode)
print("Content of file:\n" + rea.read())
rea.close()

# renaming a file
from os import *
rename("reading.txt", "rdng.txt")

# reading and writing existing file with previous data
riy = open("reading.txt", 'r+')
print(riy.read())
riy.write("\nAdding new line.")
print(riy.read())
riy.close()

# renaming a file
from os import *
rename("reading.txt", "rdng.txt")