# bank.py 
# program will prompt user to insert two cents money amount
# it will add two amounts togeter and present with euro sign and decimal point
# author: Katarina Siklodyova

numberA = int(input("Insert first amount in cents: "))
numberB = int(input("Insert second amount in cents: "))

sum = numberA + numberB
''''print(sum) '''

euro = sum //100  # this will get the total number of euros
cent = sum % 100 # this will get us the number of cents remaining.

print(f'The result is \u20ac{euro}.{cent:.02d}') #this will print out the total amount
# in euro, using the Unicode for euro symbol (u20ac)
# the :02d means that it will use 2 decimal places for cents



