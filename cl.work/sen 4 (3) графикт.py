import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = x**2
plt.figure(figsize=(10, 6), dpi=100)
plt.plot(x, y, "k--")

plt.title("graf")
plt.xlabel("x", fontsize=10)  # название осей
plt.ylabel("y", fontsize=10)

plt.xsticks([])  # засечки

plt.grid()  # сетка
# plt.savefig() #сохранение

plt.show()
