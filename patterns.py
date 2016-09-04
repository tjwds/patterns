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
thisRowInput = [2]

''' next step:  make this evaluate possible expressions for multiple inputs '''
def evaluateExpression(thisInput):
    thisExpression = []
    for z in range(thisInput):
        thisExpression.append(1)
    return thisExpression

def evaluatePossibleGoals(thisRowInput):
    holdThisInput = thisRowInput[0]
    numberOfOptions = width + 1 - holdThisInput
    paddingInBeginning = 0
    thisPossible = []
    ''' all of this is going to have to wiggle based off of mulitple possible expressions '''
    thisExpression = evaluateExpression(holdThisInput)
    for x in range(numberOfOptions):
        thisPossibleStage = []
        for y in range(paddingInBeginning):
            thisPossibleStage.append(2)
        for alpha in thisExpression:
            thisPossibleStage.append(alpha)
        while len(thisPossibleStage) != width:
            thisPossibleStage.append(2)
        paddingInBeginning += 1
        thisPossible.append(thisPossibleStage)
    return thisPossible

thisPossible = evaluatePossibleGoals(thisRowInput)
print(thisPossible)

# function to determine whether or not all elements of a list are equal
def listEqual(list):
    caseSwitch = True # bad practice but I don't know how switches work in python
    for x in list:
        if x != list[0]:
            caseSwitch = False
    return caseSwitch
    # return list == list[::-1] # this was a bad idea that is obviously incorrect

# evaluate success by process of elimination

# thisPossible = [[2, 1, 1], [2, 2, 1]] # random example
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
