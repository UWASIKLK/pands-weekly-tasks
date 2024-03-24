#program will do a histogram of a normal distribution of a 1000 valuses, mean of 5 and standad deviation of 2
#this will plot the function h(x)= x^3 in the rage of 0-10

import numpy as np
import matplotlib.pyplot as plt


x_value = np.array(range(0,10))
y_value = x_value ** 3

plt.plot(x_value, y_value, label = "h(x)=x^3", color = "red")
med = 5
dev = 2
values = 1000

np.random.seed(1)
numbers = np.random.normal(med, dev, values)

plt.hist (numbers)
plt.title("Function x^3")
plt.xlabel("X values range")
plt.ylabel("Output of (x=x^3) values")
plt.grid()
plt.legend()
plt.show()