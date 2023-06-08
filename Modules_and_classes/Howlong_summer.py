from datetime import date, datetime

today=datetime.now().date()

# print(f"Today's date is {date}")
print("Today's date is " + str(today))

target_date = date(2023, 6, 16)
day_until_target = target_date - today
x = day_until_target.days
print("Days until summer holiday:", x)
