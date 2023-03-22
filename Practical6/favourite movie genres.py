mydict = {"Comedy" : 73, "Action" : 42, "Romance" : 38, "Fantasy" : 28, "Science-fiction" : 22, "Horror" : 19, "Crime" : 18, "Documentary" : 12, "History" : 8, "War" : 7}  #a dictionary containing the information
print (mydict)
import matplotlib.pyplot as plt
import numpy as np          #import the
labels = ['Comedy', 'Action', 'Romance', 'Fantasy', 'Science-fiction', 'Horror', 'Crime', 'Documentary', 'History', 'War']       #the name of movies
sizes = [73, 42, 38, 28, 22, 19, 18, 12, 8, 7]           #The number of people who favor certain movie
plt.pie(sizes, labels=labels)          #draw the pie plot
plt.show()           #show the plot
