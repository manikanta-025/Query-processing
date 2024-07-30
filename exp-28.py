import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
fig, ax = plt.subplots(figsize=(10, 6))
ax.barh(languages, popularity)
ax.set_xlabel('Popularity (%)')
ax.set_ylabel('Programming Languages')
ax.set_title('Popularity of Programming Languages')
plt.tight_layout()
plt.show()
