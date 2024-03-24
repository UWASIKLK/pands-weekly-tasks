# **Pands Weekly Tasks**
***

### This repository contains the programs related to the problems set in the weekly tasks for programming and Scripting module. It includes solutions and references.
---
### **<ins>[The list of the programs:](https://github.com/UWASIKLK/pands-weekly-tasks/tree/main)</ins>**
* **week01:** [helloworld.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week01/helloworld.py) (additional program - [NameandAge.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week01/NameandAge.py))
* **week02:** [bank.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week02/bank.py)
* **week03:** [accounts.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week03/accounts.py)
* **week04:** [collatz.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week04/collatz.py)
* **week05:** [weekday.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week05/weekday.py)
* **week06:** [squareroot.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week06/squareroot.py)
* **week07:** [es.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week07/es.py)
* **week08:** [pottask.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week08/plottask.py)
***
## **Week 01**

The task for week 01 was to create a program _**helloworld.py**_ which would print out the "Hello World!" sentence when run. This was a very simple program using function **’print’**.

> [helloworld.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week01/helloworld.py)

---
## **Week 02**

The task for week 02 was to create a program _**bank.py**_ which would prompt the user to insert the two money amounts in cents. The program will add the two amounts and print out answer with euro sign and decimal point between the euro and cent.

This program will not verify that the entered values are correct. There is no control mechanism set up to check whether values are positive integers, floating numbers, or strings. If you select either of these options, the program sends an error message.

> [bank.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week02/bank.py)

### **<ins>Resources / References:</ins>**

#### Unicode for Euro Symbol: 
[https://www.fileformat.info/info/unicode/char/20ac/index.htm](https://www.fileformat.info/info/unicode/char/20ac/index.htm)
[https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python](https://stackoverflow.com/questions/39935857/how-can-i-print-a-euro-%E2%82%AC-symbol-in-python)

#### Zero Padding:
[https://www.askpython.com/python/string/02d-in-python#:~:text=As%20we%20have%20seen%20in%20the%20above%20example%2C%20%7B%3A02d,is%20called%20'Zero%20Padding'.](https://www.askpython.com/python/string/02d-in-python#:~:text=As%20we%20have%20seen%20in%20the%20above%20example%2C%20%7B%3A02d,is%20called%20'Zero%20Padding'.
)

---
## **Week 03**

The task for week 03 was to create the program which can sort out 10-character string of bank account numbers but for security reason we will display only the last 4 characters (the fist 6 digits will be replaced with ’X’ letter). We will name this program _**accounts.py**_. 

This program will prompt the user to enter an account number with 10 digits and it will convert the entered data into a string. It then checks the length of the input (by using len() function) and applying if /elif/else to further check the data entered. When everything is in order, it prints the account number, where the first 6 digits are replaced with "X" and the last 4 characters are displayed according to the input.

The program does not run in "loop/while" mode (I wasn't sure how to do this at this stage) to reflect what the user inserts as input (correct length (10 digits), only an integer (no floating numbers), no strings). However, if the input is not 10 digits long (if more or less than 10 digits), it will display an error/warning message.


> [accounts.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week03/accounts.py)

### **<ins>Resources / References:</ins>**

#### String Slicing:
[https://www.w3schools.com/python/python_strings_slicing.asp](https://www.w3schools.com/python/python_strings_slicing.asp)

#### Week03 Lecture:
[Wek03 Lecture](https://atlantictu-my.sharepoint.com/personal/andrew_beatty_atu_ie/_layouts/15/stream.aspx?id=%2Fpersonal%2Fandrew%5Fbeatty%5Fatu%5Fie%2FDocuments%2Fpands%20private%20%282024%29%2Fslides%2Fpands%203%2E2%20Fun%20with%20numbers%20and%20strings%2Emp4&ga=1&referrer=StreamWebApp%2EWeb&referrerScenario=AddressBarCopied%2Eview)

---
## **Week 04**

The task of week 04 was to write a program called _**collatz.py**_. This program asks the user to enter only a positive integer and perform the following calculation. At each step, calculate the next value by taking the current value and adding, if it is even number, divide it by two, but if it is odd number, multiply it by three and add one. Let the program exit if the current value is one.

My program uses a function that first checks if the inserted number is positive. If the entered number is positive, it performs the calculation as shown above until the current value is one. All calculation results are stored in a list. The function is called up at the end and the results are displayed.

> [collatz.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week04/collatz.py)

### **<ins>Resources / References:</ins>**

#### Collatz conjecture sequence:

[https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence](https://stackoverflow.com/questions/13366830/collatz-conjecture-sequence)

[https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python](https://www.educative.io/answers/how-to-generate-the-collatz-sequence-in-python)

---
## **Week 05**

The task of week 05 was to write a program called _**weekday.py**_.  This program will determine whether today is a weekend day or a day of the week.

The program first imports the ‘datetime’ module.  To find out which day is today, the program uses the function 'datetime.now()' and prints the result. I set up two string variables, one with weekend days and the other with weekdays. The program uses if/elif/else to determine whether today belongs to weekends or days of the week and print out result.

> [weekday.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week05/weekday.py)

### **<ins>Resources / References:</ins>**

#### How to get current date:

[https://www.w3schools.com/python/python_datetime.asp](https://www.w3schools.com/python/python_datetime.asp)

[https://www.geeksforgeeks.org/get-current-date-using-python/](https://www.geeksforgeeks.org/get-current-date-using-python/)

[https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/](https://www.freecodecamp.org/news/python-datetime-now-how-to-get-todays-date-and-time/)

---
## **Week 06**

The task of week 06 is to create program which will take a positive floating-point number as an input ad outputs an approximation of its square root.

As per geeksforgeeks.org (see link in references / resources) the Newton’s method of calculating square root is described as below:

> Let **N** be any number than the square root of **N** can be given by the formula:

> **_root = 0.5 * (X + (N / X))_**

> - Where **X** is any guess which can be assumed to be **N** or **1**.
> - In the above formula, **X** is any assumed square root of **N** and root is the correct square root of **N**.
> - Tolerance limit is the maximum difference between **X** and root allowed.

I created two programs for the approximate value of the square root of a given number. The result is more accurate for the second program.

> [squareroot.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week06/squareroot.py)

### **<ins>Resources / References:</ins>**

#### Square root - Newton's method:

[https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/](https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/)

[https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module](https://stackoverflow.com/questions/3047012/how-to-perform-square-root-without-using-math-module)

---
## **Week 07**

The task for week 07 was to write a program that would read in a text file and outputs all e’s that this text contains. The program should take the name of the text file from the argument in the command line.

This program must import the ‘sys’ module to pass an argument from the command line. The sys.argv represent a list of command line arguments, where the sys.argv[0] returns the script name itself, and can be ignore. The sys.argv[1] returns the first argument passed at the command line.

The program uses the open() function with an "r" to read the desired text file. To count how often both letters occur, use the count() function of lowercase "e" and uppercase "E". Separately prints occurrences of "e", "E", and overall.

> [es.py](https://github.com/UWASIKLK/pands-weekly-tasks/blob/main/week07/es.py)

### **<ins>Resources / References:</ins>**

#### sys.argv:

[https://www.knowledgehut.com/blog/programming/sys-argv-python-examples#what-are-command-line-arguments?-why-do-we-use%C2%A0them?%C2%A0](https://www.knowledgehut.com/blog/programming/sys-argv-python-examples#what-are-command-line-arguments?-why-do-we-use%C2%A0them?%C2%A0)

[https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from](https://stackoverflow.com/questions/4117530/what-does-sys-argv1-mean-what-is-sys-argv-and-where-does-it-come-from)

---
## **Week 08**

The task for week 08 is to create program called _**plottask.py**_ that display:
- A histogram of a normal distribution of a 1000 values with a mean of 5 and standard deation of 2
 - And a plot of the function h(x) = x^3
On the one set of axes.

This program must import libraries such as 'numpy' and 'matplotlib' to generate a histogram and render the function according to the above requirements. The program uses 'np.random.seed(1)', which means that the same set of numbers appears each time you run the program. Titles, labels, colour (histogram and border) and legend are set. A curve representing the function is also created.


> [plottask.py](https://github.com/UWASIKLK/pands-weekly-tasks/tree/main/week08)

### **<ins>Resources / References:</ins>**

#### Random seed:

[https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do](https://stackoverflow.com/questions/21494489/what-does-numpy-random-seed0-do)

#### Histogram:

[https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html](https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist.html)

[https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data](https://stackoverflow.com/questions/33203645/how-to-plot-a-histogram-using-matplotlib-in-python-with-a-list-of-data)

[https://www.statology.org/matplotlib-histogram-color/](https://www.statology.org/matplotlib-histogram-color/)
