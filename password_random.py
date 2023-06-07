#choose a random adjective
#choose a random noun
#choose a randomm number between 1 - 100
#choose a random punctuation character
#create a secure password = adjective+noun+number+character
#display password
#do you want another one?

import random
import string

print("Hello! Password picker copyright by AndreaT")
adjectives=["happy","exhausted","sleepy", "purple","boring","exciting","devastating"]
nouns=["house", "chimney","panda","book","owl","dolphin"]

while True:
    adjective = random.choice(adjectives).capitalize()
    noun = random.choice(nouns).capitalize()
    number = random.randrange(0,100)
    specialcharacter = random.choice(string.punctuation)
    password= adjective + noun + specialcharacter+ str(number)
    print("This is your password",password)

    answer = input("would you like another password? Y or N ")
    if answer == "N":
        break