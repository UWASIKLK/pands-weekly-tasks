# program will ask to input positive integer
# it will outputs the successive values of the following calculation:
# at each sep calculate the next value by taking the current value and
# if it si even, divide it by 2
# if it si odd, multiply by 3 and add 1
# author: Katarina Siklodyova


# defining the function which will check if the number is less than 1, if it is odd or even and 
# if entered number is even, it will devide by 2
# if number is odd it  will multiply by 3 and add 1
def fun (number):
    list = [number] #this is a list where the numbers will be saved
    if number < 1: #if number is less than 1 the list will have empty set
        print ("This is not a positive integer!")
        return []
    
    while number != 1: 
        if number % 2 == 0 : #if number is even
            number = number // 2 # it will devide by 2, I used // to make sure it is integer
                    
        else:
            number = ((number * 3 ) + 1 ) # if it is odd number, it will multiply by 3 and add 1
        list.append(number)   # this will add the calculated values to the list 
    return list

integer = int(input("Please enter a postivie integer: ")) #asking user to input the number
print (fun(integer))  # calling the function - printing out result








































