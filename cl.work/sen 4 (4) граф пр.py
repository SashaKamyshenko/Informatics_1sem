import matplotlib.pyplot as plt
import numpy as np

# labels = ['A', 'B', 'C']
# values = [1, 4, 2]

# plt.bar(labels, values) #столбчатая

# values = np.random.normal(10, 10, 1000)
# plt.hist(values, 3000) #кол-во столбцов     #гистограсмма

x = np.arange(0, 10)
y = x**2

fig = plt.figure(figsize=(10, 8))

ax1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
ax2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
ax1.plot(x, y, "y")
ax2.plot(y, x)

plt.show()
