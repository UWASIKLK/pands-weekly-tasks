#This program will ask user to input the positivie floating number
# it will calculate the approximate sqare root of entered number
# author: Katarina Sikloyova

 # this works but doesn't use function

number = float(input("Please enter a postitive number: ")) #user is prompt to insert the positive floating number
min = 1    #choosing interval were the result be located
max = number # the minimum is 1 and the maximum is the number user enter

middle = (min + max) / 2  #the 'middleis the first estimate quess of the square root
# and it is a center of the above interval
while abs((middle ** 2) - number) > 0.000001:  
    #if the square of this middle is greater than given number or less
    if middle ** 2 > number:      #if it is larger, we adjust the expected interval by 
           max = middle                     # changing its 'max' limit to 'middle'
            
    else:                           #if it is smaller, we adjust the 'min' of interval to 'middle'
            min = middle                #this will halved our interval
    middle = (min + max) / 2    #we repat all this until 'middle' is found close enough to the desired result

print("The approximate square root of", number, "is: ",middle)


#below program is using function

def sqrRoot (number):
    guess = number /2  #initialize the guess to halve of inputted number
    while True:
        middle = (guess + number/guess) / 2  # using the Newton's formula
        if abs (middle - guess) < 0.00000001: # checking if the difference between the current 
            return middle                     # quess and middle is less than the tolerance
        guess = middle

number = float(input("\nSecond program\nPlease enter a postitive number: ")) #asking user to input the number
if number <= 0:                                                 #checking if number is positive
     print("The number you entered is not a positive number!")  #if negative or zero, will print out message
else:                                                           #otherwise, calling function and
    print("The approximate square root of", number, "is: ", sqrRoot(number)) #program will print out result
