import matplotlib.pyplot as plt
import numpy as np
x,y = [1, 2, 3, 4, 5],[2, 4, 6, 8, 10]
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Simple Line Graph')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
plt.show()
