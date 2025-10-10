from math import gamma
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


def factorial(array):
    return np.array([gamma(val + 1) for val in array])


def poisson(n, n0):
    return n0**n / factorial(n) * np.exp(-n0)


x = np.arange(0, 30, 0.1)
y1 = poisson(x, 11.8)
plt.plot(x, y1, color="r")

values = (5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 23)
q = (
    0.015,
    0.05,
    0.0525,
    0.05,
    0.0875,
    0.1175,
    0.11,
    0.0925,
    0.14,
    0.0675,
    0.0475,
    0.0625,
    0.045,
    0.0175,
    0.0125,
    0.0175,
    0.005,
)
plt.bar(values, q)

plt.title("Гистограмма для t = 10 с")
plt.xlabel("n", fontsize=10)
plt.ylabel("w(n)", fontsize=10)

plt.show()
