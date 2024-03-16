# program will read in text file and account how many 'e' & 'E' letters are there
# it will print out the number of how many times letter 'e' & 'E' appeared in text.
# author: Katarina Siklodyova

import sys

with open (sys.argv[1], "r") as f:
    text = f.read()
    letter_e = text.count ("e")
    letter_E = text.count ("E")

print(f"In this text, the lovercase 'e' occured: {letter_e} times.")
print(f"The capital 'E' occured: {letter_E} times.")
print(f"The total of letters 'E & e' in this text is: {letter_E + letter_e}.")