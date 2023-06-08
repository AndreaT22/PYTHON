print("Hello!")
day=input("What day is it today?")
bank=["Monday","Tuesday","Wednesday","Thursday","Friday"]
if day in bank:
    print(f"{day} is a weekday")
else:
    print(day + " is the weekend")
