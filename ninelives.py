import random
def updateclue(guessedletter, chosenword, clue):
    index = 0
    while index < len(chosenword):
        if guessedletter == chosenword[index]:
            clue[index] = guessedletter
        index = index + 1


# welcome the user
print("Hello! Let's start the game!")


# set lives to 9
print("You have 9 lives")
lives = 9
heartsymbol = u'\u2764' #unicode character for heart symbol
print(heartsymbol*9)

# select a random secret word
secretwords = ["happy","pizza", "fairy", "money","shirt", "plane"]
chosenword = random.choice(secretwords)

# guess a letter or word
clue = list ('?????') # we want a list of 5 elements
# print(clue)

did_player_guess_correctly = False

while lives > 0:
    print(clue)
    print("lives left: " + heartsymbol*lives)
    guess=input("Guess a letter or the whole word ")
    if guess == chosenword:
        did_player_guess_correctly = True
        break
    if guess in chosenword:
        updateclue(guess, chosenword, clue)
    else:
        print("You have lost a life ")
        lives=lives-1
if did_player_guess_correctly:
    print("You won! The secret word was " + chosenword)
else:
    print("You've lost! The choosen word was " + chosenword)