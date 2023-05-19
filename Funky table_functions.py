#FUNCTIONS 
# BIF - built in functions (e.g.:print - is BIF - it is followed by brackets, whatever is inside the brackets is the argument, STR - is also a BIF)


# We are going to make our own function - multiply
def multiply():
    print ('Here\'s the multiplication table: ')
    # score=int(number)
    for i in range (1,11):
        print (str(i)+' X '+ str(score) + ' = ' + str(i*score)) #score could be 'number' as it is a string already in line 3


#1. Ask the user for a number - between 1 and 10
print(3*'Hello ')
number=input('Give me a number between 1 and 10: ')

score=int(number)
if (score > 0 and score <= 10):
     print(number,'is a great number. Thank you!') 
     multiply() # Print out the multiplication table for the number (till 10)
else:
    print("That's not allowed. Don't try to trick me!:)" )
    




