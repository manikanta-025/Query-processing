import numpy as np
import matplotlib.pyplot as plt
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]
ind = np.arange(len(means_men)) 
width = 0.35
fig, ax = plt.subplots()
men_bars = ax.bar(ind, means_men, width, yerr=std_men, label='Men', capsize=5)
women_bars = ax.bar(ind, means_women, width, bottom=means_men, yerr=std_women, label='Women', capsize=5)
ax.set_xlabel('Groups')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender with error bars')
ax.set_xticks(ind)
ax.set_xticklabels(('G1', 'G2', 'G3', 'G4', 'G5'))
ax.legend()
plt.show()
