days = ["Monday", "Tuesday", 
        "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday"]
print("These are the weekend days:")
print(days[5])
print(days[6])

print("What day is it today? Please give a number")
day = int(input())
today = days[day]
print (today)
if day > 0:
    yesterday = days[day-1] #whatever is inside the square brackets is the index of the element
else:
    yesterday = days[6]
print("Today it is", today)
print("Yesterday it was", yesterday)

