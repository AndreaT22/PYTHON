months = ["January", "February",
          "March", "April", "May",
          "June", "July", "August",
          "September", "October", "November",
          "December"]
print("These are the summer months:")
print(months[5])
print(months[6])
print(months[7])

print ("What month is it? Write 1 - 12")
month=int(input())
print("It is",months[month-1])