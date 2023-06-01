print("Hello!")
day=input("What day is it today?")
bank=["Monday","Tuesday","Wednesday","Thursday","Friday"]
for d in bank:
    if day==d:
        print(f"{day} is a weekday")
    else:
        print(day + " is the weekend")


