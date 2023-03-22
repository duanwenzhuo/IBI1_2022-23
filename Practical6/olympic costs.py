
costs = [1,8,15,7,5,14,43,40]   #store the costs
print(costs)       #print the stored values
import numpy as np
import matplotlib.pyplot as plt       #import modules
N = 8         #the number of olympic games
costs = (1,8,15,7,5,14, 43, 40)    #costs for each olympic games
ind = np.arange(N)       #the x location for each groups
width = 0.1    #the width of bars
p1 = plt.bar(ind, costs, width)          #creat the bar plot whit certain arguments: x(ind), height(costs) and width 
plt.ylabel('costs')      # y label of the bar plot
plt.xticks(ind, ('Los Angeles 1984', 'Seoul 1988', 'Barcelona 1992', 'Atlanta 1996', 'Sydney 2000', 'Athens 2003', 'Beijing 2008', 'London 2012'))
plt.title('olympic costs') #title of the plot
plt.yticks(np.arange(0,50,5))        #set the y-axis tick values with  an array of tick locations from 0 to 50 (exclusive) with a step of 5 between each value  
plt.show()   #show the plot
