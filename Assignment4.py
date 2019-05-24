#This assignment requires that you to find at least two datasets on the web which 
#are related, and that you visualize these datasets to answer a question with the 
#broad topic of sports or athletics (see below) for the region of Ann Arbor, 
#Michigan, United States, or United States more broadly.

#Data sourced from wikipedia

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime as dt
import seaborn as sns

GSW = pd.read_csv("GSW_.csv")
LAC = pd.read_csv("LAC.csv")
LAL = pd.read_csv("LAL.csv")
SK = pd.read_csv("SK.csv")
Wins_DF = pd.DataFrame({"Season":GSW["Season"], "Golden State Warriors":GSW["Win%"], "Los Angeles Lakers":LAL["Win%"], "Los Angeles Clippers":LAC["Win%"], "Sacramento Kings":SK["Win%"]})
Wins_DF["Year"] = np.arange(2000, 2019)
Wins_DF.head()

N = 19
plt.style.use('seaborn-white')
plt.figure(figsize=(9, 5))
GSW_TW = (Wins_DF["Golden State Warriors"].sum())/N
LAL_TW = (Wins_DF["Los Angeles Lakers"].sum())/N
LAC_TW = (Wins_DF["Los Angeles Clippers"].sum())/N
SK_TW = (Wins_DF["Sacramento Kings"].sum())/N
TWins = np.array([GSW_TW, LAL_TW, LAC_TW,SK_TW])
List = ("Golden State Warriors", "Los Angeles Lakers", "Los Angeles Clippers", "Sacramento Kings")
plt.bar(x = (1, 2, 3, 4), height = TWins, tick_label = List, color = ("darkblue", "purple", "red", "grey"), edgecolor = "black")
plt.title("Comparison of Californian NBA Team Total Wins (%)\nbetween 2000 and 2018", fontsize = 20)
xlocs=[i+1 for i in range(0,5)]
for i, v in enumerate(TWins):
    plt.text(xlocs[i] - 0.1, v + 0.005, str(round(v, 2)))
plt.ylim(0,0.6)
plt.ylabel("Percentage Wins (%)", fontsize = 15)
plt.yticks(fontsize = 12)
plt.xticks(fontsize = 11, rotation = 0)
plt.show()