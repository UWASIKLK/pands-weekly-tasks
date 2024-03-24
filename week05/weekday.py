# this program wil find out if today day is the weekday or not
# firstly we need to get a day of a week from Datetime
# program will check if today date is in the group of weekdays or weekends
# author: Katarina Siklodyova



from datetime import datetime  # import module

dt = datetime.now()
today = (dt.strftime("%A")) # this will return the full name of the date
print("Today is: ", today)

weekend = ("Saturday, Sunday")   # setting up weekend days
week = ("Monday, Tuesday, Wednesday, Thursday, Friday") # setting up week days

if today in week:               #checkin if today day is in within week days
    print("Yes, today is still weekday, unfortunately.")
elif today in weekend:          #checking if today day is in within weekend days
    print ("Hurrayyy! It's weekend!")
else:
    print("Don't know what is this.")  #if none of above this will be printed out