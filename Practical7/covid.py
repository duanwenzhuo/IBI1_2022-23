import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Change the working directory and read the csv file
os.chdir("C:/cygwin64/home/86188/IBI1_2022-23/Practical7")
data = pd.read_csv("full_data.csv")

# Show the second column from every 100th row from the first 1000 rows (inclusive)
print(data.iloc[:1001:100, 1])

# Use a Boolean to show "total cases" for all rows corresponding to Afghanistan
afghanistan = data["location"] == "Afghanistan"
print(data.loc[afghanistan, "total_cases"])


# Compute the mean number of new cases and new deaths on 31 March 2020
march_31 = data["date"] == "2020-03-31"
mean_new_cases = np.mean(data["new_cases"]) 
mean_new_deaths = np.mean(data["new_deaths"])
print(f"The mean new cases on this date was {mean_new_cases}.")
print(f"The mean new deaths on this date was {mean_new_deaths}.")


# Plot the new cases on 31 March as a box plot
plt.boxplot(data.loc[march_31, "new_cases"], showfliers=False)
plt.title("New cases on 31 March")
plt.ylabel("Number")
plt.show()
# Plot the new deaths on 31 March as a box plot
plt.boxplot(data.loc[march_31, "new_deaths"], showfliers=False)
plt.title("New deaths on 31 March")
plt.ylabel("Number")
plt.show()


# Plot both new cases and new deaths worldwide over time
world = data["location"] == "World"
plt.plot(data.loc[world, "date"], data.loc[world, "new_cases"], 'b', label="New cases")
plt.plot(data.loc[world, "date"], data.loc[world, "new_deaths"], 'r', label="New deaths")
plt.xlabel("Date")
plt.ylabel("Number")
plt.title("New cases and new deaths worldwide over time")
plt.xticks(data.loc[world, "date"].str.endswith("-01").to_numpy().nonzero()[0], rotation=45)
plt.legend()
plt.show()


# Answer to the question stated in file question.txt
feb_14 = data["date"] == "2021-02-14"
max_new_cases_per_million = data.loc[feb_14, "new_cases_per_million"].max()
country = data.loc[feb_14, "location"][data.loc[feb_14, "new_cases_per_million"] == max_new_cases_per_million].values[0]
print(f"The country that had the highest number of new cases per million people on 14 February 2021 was {country}.")