import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
fig, ax = plt.subplots()
ax.bar(languages, popularity)
ax.set_title('Popularity of Programming Languages')
ax.set_xlabel('Programming Languages')
ax.set_ylabel('Popularity (%)')
plt.show()
