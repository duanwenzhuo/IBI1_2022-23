import matplotlib.pyplot as plt
costs = [1,8,15,7,5,14,43,40]   
sorted_costs = sorted(costs)   #store the costs
print(sorted_costs)       #print the stored values

labels = ["Los Angeles 1984", "Atlanta 1996", "Sydney 2000", "Seoul 1988", "Athens 2003", "Barcelona 1992", "London 2012", "Beijing 2008"]

# Plot the bar chart with a title and axis labels
plt.bar(labels, sorted_costs, color="green")
plt.title("Cost of hosting the Summer Olympic Games")
plt.xlabel("City and year")
plt.ylabel("Cost (billion US dollars)")
plt.xticks(rotation=45) # Rotate the x-axis labels for better readability
plt.show()