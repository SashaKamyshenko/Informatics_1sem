import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np


data = {
    "l_20_cm_I_mA": [
        148.33,
        138.89,
        125.45,
        119.10,
        113.96,
        110.36,
        104.25,
        92.48,
        80.68,
        74.89,
        71.30,
        65.79,
        37.01,
    ],
    "l_20_cm_V_mV": [750, 700, 635, 600, 575, 550, 525, 465, 410, 380, 365, 335, 190],
    "l_30_cm_I_mA": [
        260.77,
        214.98,
        195.10,
        172.33,
        162.28,
        137.44,
        125.23,
        112.75,
        106.89,
        96.11,
        90.36,
        73.87,
        70.45,
    ],
    "l_30_cm_V_mV": [750, 650, 595, 520, 490, 420, 380, 340, 325, 290, 245, 200, 175],
    "l_50_cm_I_mA": [
        324.68,
        215.23,
        194.39,
        177.90,
        154.32,
        124.05,
        116.00,
        100.79,
        98.21,
        71.68,
        56.70,
        38.33,
        34.18,
    ],
    "l_50_cm_V_mV": [675, 440, 395, 360, 310, 250, 240, 205, 195, 145, 115, 75, 65],
}

df = pd.DataFrame(data)

xx1 = np.array(df["l_20_cm_I_mA"]) * np.array(df["l_20_cm_I_mA"])
xy1 = np.array(df["l_20_cm_I_mA"]) * np.array(df["l_20_cm_V_mV"])
xx2 = np.array(df["l_30_cm_I_mA"]) * np.array(df["l_30_cm_I_mA"])
xy2 = np.array(df["l_30_cm_I_mA"]) * np.array(df["l_30_cm_V_mV"])
xx3 = np.array(df["l_50_cm_I_mA"]) * np.array(df["l_50_cm_I_mA"])
xy3 = np.array(df["l_50_cm_I_mA"]) * np.array(df["l_50_cm_V_mV"])
k1 = np.mean(xy1) / np.mean(xx1)
k2 = np.mean(xy2) / np.mean(xx2)
k3 = np.mean(xy3) / np.mean(xx3)
