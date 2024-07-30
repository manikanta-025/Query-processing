import matplotlib.pyplot as plt
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
fig, ax = plt.subplots(figsize=(10, 6))
bars = ax.bar(languages, popularity, color='skyblue', width=0.6)
ax.set_title('Popularity of Programming Languages')
ax.set_xlabel('Programming Languages')
ax.set_ylabel('Popularity (%)')
ax.set_ylim(0, max(popularity) * 1.1)
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height,
            f'{height}%', ha='center', va='bottom')
plt.tight_layout()
plt.show()
