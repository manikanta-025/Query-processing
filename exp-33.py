import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, facecolors='none', edgecolors='b')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Distributions with Empty Circles')
plt.show()
