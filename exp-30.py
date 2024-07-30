import matplotlib.pyplot as plt
import numpy as np
means_men = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
x = np.arange(len(means_men))
width = 0.35
fig, ax = plt.subplots(figsize=(10, 6))
rects1 = ax.bar(x - width/2, means_men, width, label='Men')
rects2 = ax.bar(x + width/2, means_women, width, label='Women')
ax.set_ylabel('Scores')
ax.set_title('Scores by Group and Gender')
ax.set_xticks(x)
ax.set_xticklabels(['G1', 'G2', 'G3', 'G4', 'G5'])
ax.legend()
plt.tight_layout()
plt.show()
