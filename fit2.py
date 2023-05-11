import numpy as np
import matplotlib.pyplot as plt

# Define the known points
x = [0, 3, 4.5, 8, 11, 13]
y = [2, 3, 3, 1, 1, 2]

# Create the polynomial function
p = np.polyfit(x, y, deg=6)
poly_func = np.poly1d(p)

# Define the function f(x) = 1x + 3
f = np.poly1d([1, 3])

# Create a plot of the data points and the polynomial fit
plt.scatter(x, y, label='Data Points')
plt.plot(x, poly_func(x), label='Polynomial Fit')
plt.plot(x, f(x), label='f(x) = 1x + 3')
plt.legend()
plt.show()
