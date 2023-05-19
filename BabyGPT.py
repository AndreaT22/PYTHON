is_alive = False

print('Hello!')
person=input('What is your name?')
print('Hello!',person)
print ('Nice to meet you!',person)
feel=input('How was your day?') #one equal sign is an assignment
feeling=feel.lower() #it converts the answer to lower case
#print('I\'m happy to hear that it was',feeling)

#conditionals - if ... #the double equals sign is a comparison
if (feeling=='good'):
    is_alive= True
    print('Good day!')
elif (feeling=='ugly'):
    print('Ugly day!')
    print ('Ha-ha, that\'s funny!')
    print('I\'m sorry to hear that')
    print ('I\'m said')
elif (feeling=='not bad'):
    print ('Great!')
    print ('Good to hear that!')
    print ('I hope tomorrow will be better')
else:
    print('Sorry to hear that')


if is_alive:
    print('Well done!You\'re still alive!')
else:
    print('You\'re dead!')


