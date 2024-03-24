#program will do a histogram of a normal distribution of a 1000 valuses, mean of 5 and standad deviation of 2
#this will plot the function h(x)= x^3 in the rage of 0-10

import numpy as np              # importing libraries to create a plot
import matplotlib.pyplot as plt


x_value = np.array(range(0,10)) # setting up rage 0-10 for x-values
y_value = x_value ** 3  #setting the y-values as x^3

plt.plot(x_value, y_value, label = "h(x)=x^3", color = "red") #setting the plot
med = 5 #setting the mean
dev = 2 #setting standard deviation
values = 1000 #setting values

np.random.seed(1)                           #normal distribution with the seed set to 1
numbers = np.random.normal(med, dev, values)

plt.hist (numbers, color = "lime", ec ="red", lw=2)#creating plot using hist() function
plt.title("Function x^3")                   #setting title name
plt.xlabel("X values range")                #labeling x values
plt.ylabel("Output of (x=x^3) values")      #labeling y values
plt.grid()                                  #adding grids
plt.legend()                                #displaying legend
plt.show()                                  #displaing histogram