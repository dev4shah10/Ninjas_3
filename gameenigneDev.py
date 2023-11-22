
import os
import random
from Veggie import Veggie

NUMBEROFVEGGIES=30
def initVeggies():

    filename = input("Please enter the name of the vegetable file: ")
    #The following 2 lines are for getting a new file name in case the previous one does not exist
    while not os.path.exists(filename):
        filename = input("That file does not exist! Please enter the file name again: ")

    with open(filename, "r") as file1:
        # Although named region, it stores all the data from the file, as a list.
        filedata = []
        # the lines are stripped with trailing white spaces and appended to the filedata list
        for line in file1:
            filedata.append(line.rstrip())

    # f is a list storing split elements of filedata's first line in order to use it for creating a field.
    f = filedata[0].split(",")
    #The following code creates a 2D list representing the feild which will be used later.
    feild = []
    for x in range(0,int(f[1])):
        col=[]
        for y in range(0,int(f[2])):
            col.append(None)
        feild.append(col)

    #The following block of code creates a list of objects for all vegetables mentioned in file
    # using the Veggie constructor.
    veggieObjectslist=[]
    for j in range(0,len(filedata)):
        if j == 0:
            continue
        else:
            g = filedata[j].split(",")
            name= g[0]
            symbol= g[1]
            vegPoints= g[2]
            v=Veggie(name,symbol,vegPoints)
            veggieObjectslist.append(v)

    #The next block will add in the field random vegetables to random locations till count of 30.

    for k in range(0,NUMBEROFVEGGIES):
        #randomveggie variable is used to store an index randomly from the veggie objects' list.
        randomveggie=random.randint(0,len(veggieObjectslist)-1)
        #The veggieSym variable gets the symbol of the selected object
        veggieSym=veggieObjectslist[randomveggie].getsymbol()
        #Next 2 variables are used to get a random x and y co-ordinated location on the field.
        tryX=random.randint(0,len(feild)-1)
        tryY=random.randint(0,len(feild[0])-1)
        while feild[tryX][tryY]!=None:
            tryX = random.randint(0, len(feild)-1)
            tryY = random.randint(0, len(feild[0])-1)
        feild[tryX][tryY]=veggieSym

    # For testing, To see the field:
#     for x in range(len(feild)):
#         print(feild[x])
#     print()
#     print("\n\n",veggieObjectslist)
# initVeggies()


# def initializeGame():
#     initVeggies()
#     initCaptain()
#     initRabbits()
