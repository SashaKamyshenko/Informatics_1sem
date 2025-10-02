import matplotlib.pyplot as plt
import numpy as np


# plt.pie([0.5, 0.5, 0.1], labels = ['A', 'B', 'C'])  #круговая


fig = plt.figure(figsize=(10, 8))
ax1 = fig.add_subplot(211)  # расположение (?)
ax2 = fig.add_subplot(212)

# plt.subplots_adjust(...) #растояние между гр

ax1.set_title("G1")

values = np.random.normal(0, 20, 1000)
ax1.hist(values, 100)
ax2.plot(np.arange(0, 5, 1), np.arange(0, 5, 1) ** 2)
ax2.plot(np.arange(0, 5, 1), np.arange(0, 5, 1) ** 3)  # два гр на одной ск


plt.show()
