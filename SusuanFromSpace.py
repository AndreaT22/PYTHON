print("Hello my name is Susan from Space")
name=input("'What's your name?")
#print("Hello" + name + "I am from the year 2210 and I am 20 years old")
print(f"Hello {name}. I am from the year 2210 and I am 20 years old") #f - is a formatted string
age=int(input("How old are you?"))
#future_age=(int(age) + (2210-2023))
future_age=(age + (2210-2023))
print(f"Wow, by 2210 you will be {future_age} that is really old!")
#print("Wow, by 2210 you will be " + str(future_age) + " that is really old!")
music=input("What music are you into?")
print (f"I have not heard of {music}")
#print ("I have not heard of " + music)


#string interpolation:
# declaring a string variable
n = "Geek"

# append a string within a string
print("Hey, %s!" % n)
print("Hey, %s %s %s!" % (n, music, name))