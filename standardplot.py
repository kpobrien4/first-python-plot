import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)  # Create a list of evenly-spaced numbers over the range
plt.plot(x, np.exp(x))       # Plot the sine of each x point
plt.show()                   # Display the plot

y = np.linspace(0,20,100)
plt.plot(y, np.sqrt(y))
plt.show()