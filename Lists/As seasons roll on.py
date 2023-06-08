seasons = ["Winter", "Spring", "Summer", "Autumn"]
month = int(input("What month is it? (1-12)"))
if month < 3 or month == 12:
    season = 0
elif 3 <= month <= 5:
    season = 1
elif 5 < month < 9:
    season = 2
else:
    season = 3
print("It's", seasons [season])
