import random

'''
Allows the user to specify a certain number of dice to generate, 
how many sides they should all have, and how many times each should be rolled, then
print results
'''

'''
Represents a Dice object
'''
class dice:
    
    numSides = 0

    #default initialization to 6 sides
    def __init__(self):
        self.numSides = 6
    
    #allows a specifc number of sides 
    def __init__(self, sides):
        self.numSides = sides
    
    def printSides(self):
        print"sides: ", self.numSides
    
    '''
    simulates rolling the die byreturning a number between 1
    and the number of sides the die has
    '''
    def roll(self):
        return random.randint(1, self.numSides)

'''
ask the user for the number of dice to create, as well as the number of sides the dice 
should have, makes a list of the dice and inits them, them ask them how many times to
roll the dice and prints the results
'''
def main():
    numDice = input("Enter the number of dice to generate: ")
    sides = input("Enter the number of sides the dice should have: ")
    diceList = list()
    #making the dice
    for x in range(numDice):
        diceList.append(dice(sides))
    rollPerDie = input("How many times should each dice be rolled? ")
    #rolling the dice
    for j in range(numDice):
        for i in range(rollPerDie):
            print("Die {0}, roll {1} - result: {2}".format(j+1, i+1, diceList[i].roll()))
            
main()
