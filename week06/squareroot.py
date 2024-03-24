#This program will ask user to input the positivie floating number
# it will calculate the approximate sqare root of entered number
# author: Katarina Sikloyova

 # this works but doesn't use function

number = float(input("Please enter a postitive number: "))
min = 1    #I choose the interval for the result
max = number # the minimum is 1 and the maximum is the number user enter

middle = (min + max) / 2  #the 'middlel is the first estimate quess of the square root and it is a middle of the above interval
while abs((middle ** 2) - number) > 0.000001:  
    #we find out if the square of this middle is greater than given number or less
    if middle ** 2 > number:      #if it is larger, we adjust the expected interval by hanging its 'max' limit to middle
            max = middle
    else:                           #if it is smaller, we adjust the 'min' if interval to middle
            min = middle                #this will halved our interval
    middle = (min + max) / 2    #we repat all this until middle is found close enough to the desired result

print("The approximate square root of", number, "is: ",middle)


#below program is using function

def sqrRoot (number):
    guess = number /2
    while True:
        middle = (guess + number/guess) / 2
        if abs (middle - guess) < 0.00000001:
            return middle
        guess = middle

number = float(input("\nSecond program:\nPlease enter a postitive number: "))
if number <= 0:
     print("The number you entered is not a positive number!")
else:
    print("The approximate square root of", number, "is: ", sqrRoot(number))
