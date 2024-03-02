# program wil read bank acocunt number of 10 digits
# and it will outputs the last 4 digits
# the first 6 digits will be replaced by 'X'
# author: Katarina Siklodyova

account = input("Please enter an 10 digits account number: ")
account_string = str(account)
account_length = len(account_string)

first_digits = 'X'*6 # replacing first 6 digits with 'X'

#checking the length of the inputed digits
if account_length <= 0 and account_length > 10:
    print ("This is not correct number. Please try again.")

elif account_length < 10:
    print ("Incorrect account number - not enough digits!")

elif account_length > 10:
   print ("Incorrect acount number - too much digits!")

else:
   print ("Your account is: {}{}" .format (first_digits, account[6:])) 
   # printing the first 6 digits as 'X' and the last 4 digits from the inputed number
   # once the length of input was checked