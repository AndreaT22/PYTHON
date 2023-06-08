#print("What day is it today?")
#day=int(input("Write a number "))

#modules and classes
from datetime import datetime 
day=datetime.now().weekday()



if day < 4:
    print("It's a weekday")
    remaining=5-day
    print(remaining, "days until the weekend!")
elif day==4:
    print("You're almost there!")
else:
    print("It's the weekend already!")