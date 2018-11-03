import matplotlib.pyplot as plt
import numpy as np

n = 50    # data size
X = np.random.normal(0, 1, n)
Y = np.random.normal(0, 1, n)
# X = np.random.rand(n)
# Y = np.random.rand(n)
T = np.arctan2(Y, X)    # for color later on

plt.scatter(X, Y, s=70, alpha=.5, c=T)
# plt.xlim(-1.5, 1.5)
# plt.ylim(-1.5, 1.5)
# plt.xticks(())  # ignore xticks
# plt.yticks(())  # ignore yticks

plt.show()