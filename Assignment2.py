#For this assignment, you must:
#Read the documentation and familiarize yourself with the dataset, then write 
#some python code which returns a line graph of the record high and record low 
#temperatures by day of the year over the period 2005-2014. The area between the 
#record high and record low temperatures for each day should be shaded.
#Overlay a scatter of the 2015 data for any points (highs and lows) for which 
#the ten year record (2005-2014) record high or record low was broken in 2015.
#Watch out for leap days (i.e. February 29th), it is reasonable to remove these 
#points from the dataset for the purpose of this visualization.
#Make the visual nice! Leverage principles from the first module in this course 
#when developing your solution. Consider issues such as legends, labels, and chart junk.
#The data you have been given is near Ann Arbor, Michigan, United States.

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib.dates as mdates
import datetime as dt

DF_Main = pd.read_csv("fb441.csv")
DF_Main = DF_Main.sort_values("Date")

DF_Main["Date"] = DF_Main["Date"].astype("datetime64")

#Creating Min and Max Data Frames
DF_Main["New_Date"] = DF_Main["Date"].apply(lambda x: dt.datetime.strftime(x,'%m-%d'))
DF_Main["New_Year"] = DF_Main["Date"].apply(lambda x: dt.datetime.strftime(x, "%Y"))
DF_Main["Date"] = DF_Main["Date"].apply(lambda x: dt.datetime.strftime(x,'%Y-%m-%d'))

DF_Edited = DF_Main.where(DF_Main["New_Year"] != "2015").dropna()

DF_Max = DF_Edited.where(DF_Edited["Element"] == "TMAX").dropna()
DF_Max = DF_Max.set_index(["New_Date"]).groupby(level=0)["Data_Value"].agg({"Max":max})
DF_Max["Date"] = DF_Max.index
DF_Max = DF_Max.where(DF_Max["Date"] != "02-29").dropna()
DF_Max = DF_Max.drop("Date", axis = 1)

DF_Min = DF_Edited.where(DF_Edited["Element"] == "TMIN").dropna()
DF_Min = DF_Min.set_index(["New_Date"]).groupby(level=0)["Data_Value"].agg({"Min":min})
DF_Min["Date"] = DF_Min.index
DF_Min = DF_Min.where(DF_Min["Date"] != "02-29").dropna()
DF_Min = DF_Min.drop("Date", axis = 1)

#Creating 2015 Data Frame
DF_2015 = DF_Main.where(DF_Main["New_Year"]=="2015").dropna()
DF_2015_Max = DF_2015.where(DF_2015["Element"]=="TMAX").dropna()
DF_2015_Max = DF_2015_Max.set_index(["New_Date"]).groupby(level=0)["Data_Value"].agg({"2015Max":max})
DF_2015_Max["Date"] = DF_2015_Max.index
DF_2015_Max = DF_2015_Max.where(DF_2015_Max["Date"] != "02-29").dropna()
DF_2015_Max = DF_2015_Max.drop("Date", axis = 1)

DF_2015_Min = DF_2015.where(DF_2015["Element"]=="TMIN").dropna()
DF_2015_Min = DF_2015_Min.set_index(["New_Date"]).groupby(level=0)["Data_Value"].agg({"2015Min":min})
DF_2015_Min["Date"] = DF_2015_Min.index
DF_2015_Min = DF_2015_Min.where(DF_2015_Min["Date"] != "02-29").dropna()
DF_2015_Min = DF_2015_Min.drop("Date", axis = 1)

#Combining Data frames
DF_Plot = pd.concat([DF_Max, DF_Min, DF_2015_Max, DF_2015_Min], axis = 1, join = "outer")
DF_Plot["Hotter"] = DF_Plot["2015Max"].where(DF_Plot["2015Max"] > DF_Plot["Max"])
DF_Plot["Colder"] = DF_Plot["2015Min"].where(DF_Plot["2015Min"] < DF_Plot["Min"])
Hotter = (DF_Plot["Hotter"]) / 10
Colder = (DF_Plot["Colder"]) / 10

#Creating plot
import seaborn as sns
sns.set(style="white", rc={'axes.facecolor':'white'})
fig, ax = plt.subplots(figsize=(10,7))
ax.set_prop_cycle('color', ['red', 'blue'])

x = np.arange('2015-01-01', '2016-01-01', dtype='datetime64[D]')
MAX = np.array((DF_Max["Max"]) / 10)
MIN = np.array((DF_Min["Min"]) / 10)

plt.plot(x, MAX, "--", label = "Maximum temperature recorded (2005-2014)")
plt.plot(x, MIN, "--", label="Minimum temperature recorded (2005-2014)")
plt.scatter(x, Hotter, c = "red", edgecolors = "black", label = "2015 temperatures exceeding the maximum")
plt.scatter(x, Colder, c = "blue", edgecolors = "black", label = "2015 temperature exceeding the minimum")
ax.fill_between(x, MIN, MAX, facecolor='grey', alpha=0.15)
plt.xlim("2015-01-01 00:00:00", "2015-12-31 00:00:00")

months = mdates.MonthLocator()  # every month
monthFmt = mdates.DateFormatter('%m-%d')

ax.xaxis.set_major_locator(months)
ax.xaxis.set_major_formatter(monthFmt)

plt.xticks(rotation=90)

plt.title("Daily Temperature Record Highs and Lows for 2005-2014\n(Ann Arbor, Michigan, United States)", fontsize=25, color="black")
plt.ylabel("Temperature (°C)", fontsize=20, color="black")
plt.xlabel("Date (month-day)", fontsize=20, color="black")
plt.yticks(fontsize=20)
plt.xticks(fontsize=20)
plt.legend(frameon=False, shadow=False, fontsize=11, facecolor="white")

plt.show()