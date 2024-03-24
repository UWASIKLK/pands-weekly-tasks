# program will read in text file and account how many 'e' & 'E' letters are there
# it will print out the number of how many times letter 'e' & 'E' appeared in text.
# author: Katarina Siklodyova

import sys  # importing sys module

# sys.argv is a list containing the command-line arguments which are passed to the script
# once we run this script with arguments, python will capture it and save in a list - sys.argv
# sys.argv[1] is the first command line argument which is passed to the script, I am using
# the sys.argv[1] to read from: python e_letter.py schumman.txt

with open (sys.argv[1], "r") as f:  # opening the file
    text = f.read()
    letter_e = text.count ("e")     #counting lowercase letter e
    letter_E = text.count ("E")     #counting uppercase letter E

print(f"In this text, the lovercase 'e' occured: {letter_e} times.") # printint out 'e'
print(f"The uppercase 'E' occured: {letter_E} times.") # printing out 'E' 
print(f"The total of letters 'E & e' in this text is: {letter_E + letter_e}.") # printing out totals e + E