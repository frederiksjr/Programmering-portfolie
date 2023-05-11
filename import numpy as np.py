import numpy as np
import matplotlib.pyplot as plt

# Define the known points
x = np.array([0, 3, 4.5, 8, 11, 13])
y = np.array([2, 3, 3, 1, 1, 2])

# Create the polynomial function
p = np.polyfit(x, y, deg=6)
poly_func = np.poly1d(p)

# Plot the data and the polynomial function
plt.scatter(x, y)
plt.plot(x, poly_func(x), color='red')

# Add labels and title
plt.xlabel('x')
plt.ylabel('y')
plt.title('Linear Polynomial Fit')

# Show the plot
plt.show()

# Print the polynomial function
print(poly_func)
