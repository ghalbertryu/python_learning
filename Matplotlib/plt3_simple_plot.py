import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 100000)
y = 2*x + 1
# y = x**2
# y = 3 * x**5 + 4 * x**3 + 6 * x**2 + 9 * x + 2
plt.plot(x, y)
plt.show()