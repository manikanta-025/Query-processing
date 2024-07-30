import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
x = np.random.randn(50)
y = np.random.randn(50)
sizes = np.random.randint(10, 100, 50)
plt.scatter(x, y, s=sizes, alpha=0.7)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Randomly Sized Balls')
plt.show()
