
# Create a dictionary containing the information in the table 
mydict = {"Comedy" : 73, "Action" : 42, "Romance" : 38, "Fantasy" : 28, "Science-fiction" : 22, "Horror" : 19, "Crime" : 18, "Documentary" : 12, "History" : 8, "War" : 7} 
print (mydict)

requested_genre = "Action"
print(f"The number of university students who prefer {requested_genre} is {mydict[requested_genre]}.")