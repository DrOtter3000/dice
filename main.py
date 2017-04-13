"""
    @autor Tristan xtristrix Eberhart
    @version 1.0
    @license Public GNU3 
"""

import random

random.seed

# This Process checks the input for being > value 'figure'
def figureCheck(figure, max):
    while (figure < max):
        print (figure, " is not a valid value. Please repeat the input and choose a valid one:")
        figure = int(input())

    print ("ok")
    return(figure)


# This Process defines the number of sides, the dice has.
def sides():
    print ("Please enter the number of sides, this kind of dices has:")
    number = int(input())
    side = figureCheck(number, 1)
    return side


# This process defines the numger of thrown dices of the type
def shots():
    print ("Please enter the number of Dices you want to throw of this type:")
    number = int(input())
    shot = figureCheck(number, 1)
    return shot


# This process calculates the result for a number of shots with a dice of one type
def getResult():
    result = 0
    maxSide = sides()
    numOfShots = shots()
    for i in range(1, numOfShots +1):
        interimResult = random.randint(1, maxSide)
        result = result + interimResult
        print ("Result of shot number ",i, " with ", numOfShots,"D",maxSide, " is ", interimResult)
    print ("The acutal result is ", result, ". Are there some modifications in this inning? (If no write 0.")
    boni = int(input())
    result = result + boni
    print ("the result is ", result)
    return (result)


# Here starts the main method
answer = 1
result = getResult()
while (answer == 1):
    print ("Do you want to roll another kind of dices?")
    letter = input()
    if (letter == "y"):
        answer = 1
        result = result + getResult()
    elif (letter == "n"):
        answer = 2
    else:
        print ("Your input is incorrect, please choose again.")

print (result)