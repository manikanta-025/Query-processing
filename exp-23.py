import matplotlib.pyplot as plt
x = []
y = []
with open('text.txt', 'r') as file:
    for line in file:
        values = line.strip().split()
        x.append(float(values[0]))
        y.append(float(values[1]))
plt.plot(x, y)
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.title('Line Plot from File Data')
plt.show()
