import matplotlib.pyplot as plt
import numpy as np
fig, axs = plt.subplots(2, 2, figsize=(12, 10))
x = np.linspace(0, 10, 100)
axs[0, 0].plot(x, np.sin(x))
axs[0, 0].set_title('Line Plot')
x = np.random.rand(50)
y = np.random.rand(50)
axs[0, 1].scatter(x, y)
axs[0, 1].set_title('Scatter Plot')
x = ['A', 'B', 'C', 'D', 'E']
y = [23, 45, 56, 78, 32]
axs[1, 0].bar(x, y)
axs[1, 0].set_title('Bar Plot')
data = np.random.randn(1000)
axs[1, 1].hist(data, bins=30)
axs[1, 1].set_title('Histogram')
plt.tight_layout()
plt.show()
