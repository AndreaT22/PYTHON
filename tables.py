#1. Ask the user for a number - between 1 and 10
print(3*'Hello ')
number=input('Give me a number between 1 and 10: ')

score=int(number)
# if (int(number)>0 and int(number)<=10 )
if (score > 0 and score <= 10):
     print(number,'is a great number. Thank you!')
else:
    print("That's not allowed. Don't try to trick me!:)" )



print ('Here\'s the multiplication table: ')
#2. Print out the multiplication table for the number (till 10)
#for x in range(25,score):
#print(x*x)
score=int(number)
for i in range (1,11):
    # print (i*score)
    print (str(i)+' X '+ str(score) + ' = ' + str(i*score)) #score could be 'number' as it is a string already in line 3
