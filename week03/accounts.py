# program wil read bank acocunt number of 10 digits
# and it will outputs the last 4 digits
# the first 6 digits will be replaced by 'X'
# author: Katarina Siklodyova

account = input("Please enter an 10 digits account number: ") # asking user to input the number
account_string = str(account)   # the inputed number is convert to the type : string
account_length = len(account_string) # this will return the length of the objet - we need 10 digits

first_digits = 'X'*6 # replacing first 6 digits with 'X'

#checking the length of the inputed digits, if the object falls within 10
if account_length <= 0 and account_length > 10:              #if it is less or more than 10 
    print ("This is not correct number. Please try again.")  #this sentence will appear
                                                            
elif account_length < 10:
    print ("Incorrect account number - not enough digits!") #if the length is less than 10
                                                            #this message will appear

elif account_length > 10:                                  #if length is more than 10
   print ("Incorrect acount number - too much digits!")    #this message will appear

else:
   print ("Your account is: {}{}" .format (first_digits, account[6:])) 
   # printing the first 6 digits as 'X' and the last 4 digits from the inputed number
   # once the length of input was checked as per above