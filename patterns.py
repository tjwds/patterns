# patterns.py

# CLI
## user input
width = 3

# 2D array rotation
def rotateArray(successArray):
    return list(zip(*successArray[::-1]))
    # note:  this returns each item in the list as a tuple, which is sort of annoying

# initialize patterns successArray
successArray = []
for number in range(width):
    successArray.append([0] * width)

# evaluation of possible goals

# function to determine whether or not all elements of a list are equal
def listEqual(list):
    caseSwitch = True # bad practice but I don't know how switches work in python
    for x in list:
        if x != list[0]:
            caseSwitch = False
    return caseSwitch
    # return list == list[::-1] # this was a bad idea that is obviously incorrect

# evaluate success by process of elimination
thisPossible = [[2, 1, 1], [2, 2, 1]] # random example
thisSuccessArray = [0] * width # this will need to grab from successArray later
thisSuccessHold = []
numPossibilities = len(thisPossible)
for number in range(width):
    for eachElement in range(numPossibilities):
        thisSuccessHold.append(thisPossible[eachElement][number])
    if listEqual(thisSuccessHold):
        thisSuccessArray[number] = thisSuccessHold[0]
    thisSuccessHold = []

print(thisSuccessArray)
