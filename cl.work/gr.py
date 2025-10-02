import matplotlib.pyplot as plt
import numpy as np

plt.plot(
    np.arange(0, 5, 1), np.arange(0, 5, 1) ** 2, label=r"$x^2$"
)  # подписывать график
plt.legend(loc=4)  # вывод легенды, какой угол


plt.show()
