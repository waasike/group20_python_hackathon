# BUS FARE CHALLENGE - Task One (Day 1)
import datetime 

date = datetime.datetime.now()
day = date.strftime("%A")[0:3]
weekdays = ["Mon", "Tue", "Wed", "Thu", "Fri"]

print("Date :", date)
print("Day:", day)

if day in weekdays:
    print("Fare:", 100)
elif day == "Sat":
    print("Fare:", 60)
elif day == "Sun":
    print("Fare:", 80)