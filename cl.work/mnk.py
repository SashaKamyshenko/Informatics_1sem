import matplotlib.pyplot as plt
import numpy as np

x = [1.01, 2.59, 3.03, 5.04, 7.03]
y = [0.41, 0.84, 1.11, 3.22, 5.0]


plt.scatter(x, y)  # просто точки, не соед
plt.errorbar(x, y, yerr=0.2, xerr=0.1, linestyle="none")  # кресты погрешности


mnk = np.polyfit(x, y, 4)  # коэф мнк
z = np.poly1d(mnk)
plt.plot(np.linspace(0, 10, 100), [z(i) for i in np.linspace(0, 10, 100)])

print(z)

plt.show()
