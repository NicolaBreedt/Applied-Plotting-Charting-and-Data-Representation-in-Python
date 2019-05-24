#Easiest option: Implement the bar coloring as described above - a color scale 
#with only three colors, (e.g. blue, white, and red). Assume the user provides 
#the y axis value of interest as a parameter or variable.

# Use the following data for this assignment:
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df

import matplotlib.pyplot as plt
from scipy.stats import sem, t
from scipy import mean
confidence = 0.95

_1992 = np.array(df.iloc[0,:])
_1993 = np.array(df.iloc[1,:])
_1994 = np.array(df.iloc[2,:])
_1995 = np.array(df.iloc[3,:])

M_1992 = _1992.mean()
M_1993 = _1993.mean()
M_1994 = _1994.mean()
M_1995 = _1995.mean()
M_array = (M_1992, M_1993, M_1994, M_1995)

#1992
data = _1992
n = len(data)
m = mean(data)
std_err = sem(data)
h_1992 = std_err * t.ppf((1 + confidence) / 2, n - 1)

#1993
data = _1993
n = len(data)
m = mean(data)
std_err = sem(data)
h_1993 = std_err * t.ppf((1 + confidence) / 2, n - 1)

#1994
data = _1994
n = len(data)
m = mean(data)
std_err = sem(data)
h_1994 = std_err * t.ppf((1 + confidence) / 2, n - 1)

#1995
data = _1995
n = len(data)
m = mean(data)
std_err = sem(data)
h_1995 = std_err * t.ppf((1 + confidence) / 2, n - 1)

SE_array = (h_1992, h_1993, h_1994, h_1995)

y = input("Enter a number from the y-axis")

y = int(y)
type(y)

Colour = []
for i, j in zip(M_array, SE_array):
    if (i + j > y) and (i - j > y):
        c = "red"
        Colour.append(c)
    elif (i + j < y) and (i - j < y):
        c = "blue"
        Colour.append(c)
    else:
        c = "white"
        Colour.append(c)

fig = plt.figure()
ax = fig.add_subplot(111)
        
        
ax.bar(x = (1, 2, 3, 4), 
        height = M_array, 
        yerr = SE_array, 
        tick_label = ["1992", "1993", "1994", "1995"],
        capsize = 5, 
        color = Colour, 
        edgecolor = "black")

ax.axhline(y, color="gray")
ax.text(1.02, y, y, va='center', ha="left", bbox=dict(facecolor="w",alpha=0.5),
        transform=ax.get_yaxis_transform())

plt.show()    
#plt.savefig("Colour Bars.jpeg")