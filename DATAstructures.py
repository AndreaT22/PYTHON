# this is a comment
# print ('Hello')
# variables
# These are a few of my favourite things - Sound of Music

Raindrops_on_roses=101 #this is a variable that stores an integer (whole number)
# str(Raindrops_on_roses) - we converted integar to a string by adding 'str'
print('I counted ' + str (Raindrops_on_roses) + ' raindrops in the garden in the morning')

Whiskers_on_kittens=8.5 #this is another 'box' and it stores another number (float number - not whole)
print(Whiskers_on_kittens) #this is a variable which includes a float numbers
print ('I saw ' + str (Whiskers_on_kittens) + ' whiskers on each of my kittens') #we made the variable a string by adding str and putting the variable in brackets (it was needed cause it includes a float number)

brown_paper_packages='surprise' # this is a string held by 'pegs'
print ('I prepared a ' + brown_paper_packages + ' for my grandma') # you don't need to make this a STR cause it's already a string - surprise
print(brown_paper_packages)


#boolean vairable - has only true/false - booleans are named with IS
is_alive=True



# a list variable
friends_and_family=['Geri', 'Anyu', 'Zoli', 'Apu', 'Kinga'] # this is a list of names USE SQUARED BRACKETS
friends_and_family.append('Aurelia') # we added - appended - Aurelia to the end bc. we didn't add a number
print(friends_and_family)
print(friends_and_family[2]) # this printed only the 2nd item on the list
friends_and_family.insert(3,'Saurabh') #this added - insertec - the name in the 3rd place (or 4th because it starts to count from 0 just to make things more complicated)
print(friends_and_family)
Geri='0429'

# dictionary = key : value - pairs - each of them has an index (sets don't have an index)
birthdays={'Geri':'0429', 'Anyu':'0522','Zoli':'0914'}
print(friends_and_family)
print(birthdays)
birthdays['Saurabh']='0507' 
birthdays['Aurelia']='0428'
print(birthdays)

#sets - is unordered collections of data
fruits = {'apple', 'banana', 'cherries', 'grapes', 'apple'}
print(fruits) # it doesn't repeat any elements / if you run it mulitple time, you might get a different order of the elements

#tuples - collection of data / no brackets around it
hippie_stuff = 'beads', 'guitar', 420, 'incense', 'tie-dye shirt', 'sandals'
print(hippie_stuff [1])


score=100
score=score+1
print('your score is ' + str (score))