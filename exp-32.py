import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.randn(100)
y = np.random.randn(100)
plt.scatter(x, y, alpha=0.7, edgecolors='w', s=100)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Distributions')
plt.show()
