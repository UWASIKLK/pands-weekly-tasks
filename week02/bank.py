# bank.py 
# program will prompt user to insert two cents money amount
# it will add two amounts togeter and present with euro sign and decimal point
# author: Katarina Siklodyova

numberA = int(input("Insert first amount in cents: "))
numberB = int(input("Insert second amount in cents: "))

sum = numberA + numberB
''''print(sum) '''

result = sum / 100
''''print(result)'''

print('The result is €', result)
