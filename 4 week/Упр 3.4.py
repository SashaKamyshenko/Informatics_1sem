import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = pd.read_csv("C:/MyPythonProjects/4 week/iris_data.csv")  # читаем через формат csv

species = set(df["Species"])  # неповторяющиеся

plt.subplot(2, 1, 1)
plt.pie([list(df["Species"]).count(i) for i in species], labels=species)

d = {"Petals <= 1.2": 0, "Petals 1.2 - 1.5": 0, "Petals > 1.5": 0}
for i in list(df["PetalLengthCm"]):
    if i <= 1.2:
        d["Petals <= 1.2"] += 1
    elif i > 1.2 and i < 1.5:
        d["Petals 1.2 - 1.5"] += 1
    else:
        d["Petals > 1.5"] += 1

plt.subplot(2, 1, 2)
plt.pie(list(d.values()), labels=list(d.keys()))

plt.show()

print(df.loc[1])
print(df["Species"])
print(df)
