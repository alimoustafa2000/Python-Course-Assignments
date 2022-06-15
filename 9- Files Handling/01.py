i = 0

for file in range(1,51,1):

    if file == 25:

        filename = "special-text.txt"
        file = open(filename,"w")
    
    else:

        filename = f"txt{file}.txt"
        file = open(filename,"w")

        i += 1
        if i < 25:
            file.write(f"Elzero Web School => {i}\n")

        if i >= 25:
            file.write(f"Elzero Web School => {i + 1}\n")


import os


# To print Current Working Directory

print(os.getcwd())
print("=" * 40)


# To print file name

myfile = open(r"C:\Users\A L I\Desktop\Python\assign.py","r")

print(myfile.name)
print("=" * 40)


# To print number of files inside the directory

files_num = len(os.listdir(r"C:\Users\A L I\Desktop\Python"))
print(f"Number of files is : {files_num}")
print("=" * 40)


# To write "Appended => Elzero Web School" in txt1.txt 50 times

myfile = open(r"C:\Users\A L I\Desktop\Python\txt1.txt","a")

myfile.write("Appended => Elzero Web School\n" * 50)


# To print number of lines in a file

myfile = open(r"C:\Users\A L I\Desktop\Python\txt1.txt","r")
lines = len(myfile.readlines())
print(f"Number Of Lines Is => {lines}")
print("=" * 40)


# To print number of words in a file

myfile = open(r"C:\Users\A L I\Desktop\Python\txt1.txt","r")
words = len(myfile.read().split())
print(f"Number Of Words Is => {words}")
print("=" * 40)


# To print number of Characters in a file

myfile = open(r"C:\Users\A L I\Desktop\Python\txt1.txt","r")
Characters = len(myfile.read().replace(" ","").replace("\n",""))
print(f"Number Of Characters Is => {Characters}")
print("=" * 40)


# To print number of specific Character in a file

myfile = open(r"C:\Users\A L I\Desktop\Python\txt1.txt","r")
Character_l = myfile.read().count('l')
print(f"Number Of Character[l] Is => {Character_l}")
print("=" * 40)


# To remove the last 10 files

x = 50

import os

for file in os.listdir(r"C:\Users\A L I\Desktop\Python"):

        os.remove(rf"C:\Users\A L I\Desktop\Python\txt{x}.txt")

        x-=1

        if x == 40:

            break
