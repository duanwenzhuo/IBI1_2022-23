import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("C: cygwin64/home/86188/IBI1_2022-23/Practical7")
covid_data = pd.read_csv("full_data.csv")
covid_data.iloc[[2,102,202,302,402,502,602,702,802,902], ]
covid_data.loc[ : ,"location"]
is_Afghanistan = covid_data["location"] == "Afghanistan"  
covid_data_Afghanistan = covid_data[is_Afghanistan]
print (covid_data_Afghanistan)
new_data = covid_data["date"] == "2022/3/31"
new_data.loc[1,["location", "new_cases", "new_deaths"]]
all_data = np.random.uniform(0,std,size=100)
plt.boxplot(all_data, vert = True, patch-artist = true)
plt.show
