import re

userCont = True
againLoop = 1


#Checks that input is the length of the choices given
def checkLength(x):
    length = len(x)

    if length == 1:
        return True
    elif length == 4:
        return True
    elif length == 5:
        return True
    elif length == 8:
        return True
    else:
        return False


#Bad Inputs
def badInput():
    print("Please only type in the given choices.\n")


#Using arrays are easier/more compact than using if/else statements
def whichChoice(x):
    reChoices = [
        'r',
        'rock',
        'p',
        'paper',
        's',
        'scissors'
    ]

    returnChoice = {
        'r': reChoices[0],
        'p': reChoices[1],
        's': reChoices[2]
    }

    for check in reChoices:
        if x == check:
            return returnChoice[x[0]]
            break
    else:
        badInput()


#Gives computer's response
def compAns(x):
    if x == 'r':
        print("Computer chose Paper")
    elif x == 'p':
        print("Computer chose Scissors")
    elif x == 's':
        print("Computer chose Rock")

#Checks if they still want to play
def askAgain():
    global againLoop

    while againLoop == 1:
        again = input("Try again? y/n or spell it out\n")
        if again.strip().lower().startswith('y'):
            againLoop = 0
            return True
        elif again.strip().lower().startswith('n'):
            againLoop = 0
            return False
        else:
            badInput()
    else:
        print("Goodbye.")


#Creates a loop so user can replay as much times as they want
#Serves as the main function
while userCont == True:
#Initializing variables used in order of appearance
    choice = ""
    whatChoice = 0

#Asks for user's choice
    print( "Choose Rock, Paper, or Scissors (R, P, S, or spell it out)" )
    choice = input()

    #Check string length
    choiceLength = checkLength(choice.strip().lower())
    if choiceLength:
        whatChoice = whichChoice(choice.strip().lower())
    else:
        badInput()

#whatChoice is set by whichChoice function
    

#Gives computer's answer
    compAns(whatChoice)

    replay = askAgain()
    if replay:
        userCont = True
        print()
        againLoop = 1
    else:
        userCont = False
else:
    print("Goodbye.")

