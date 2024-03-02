# this program wil find out if today day is the weekday or not
# firstly we need to get a day of a week from Datetime
# program will check if today date is in the group of weekdays or weekends
# author: Katarina Siklodyova



from datetime import datetime

dt = datetime.now()
today = (dt.strftime("%A")) # this will return the full name of the date
print("Today is: ", today)

weekend = ("Saturday, Sunday")
week = ("Monday, Tuesday, Wednesday, Thursday, Friday")

if today in week:
    print("Yes, today is still weekday, unfortunately.")
elif today in weekend:
    print ("Hurrayyy! It's weekend!")
else:
    print("Don't know what is this.")