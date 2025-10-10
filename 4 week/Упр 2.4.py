import matplotlib.pyplot as plt
import numpy as np

values1 = np.random.normal(10, 10, 100)
plt.subplot(3, 1, 1)
plt.hist(values1, 100)

values2 = np.random.normal(10, 10, 1000)
plt.subplot(3, 1, 2)
plt.hist(values2, 100)

values3 = np.random.normal(10, 10, 10000)
plt.subplot(3, 1, 3)
plt.hist(values3, 100)

plt.show()
