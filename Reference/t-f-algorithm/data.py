""" SAMPLE
In this file you can find sample data which could be used
into the TrafficFlowMod class in model.py file
"""

# Graph represented by directed dictionary
# In order: first ("5", "7"), second ("5", "9"), third ("6", "7")...
graph = [
    ("1", ["2", "3"]),
    ("2", ["3", "4"]),
    ("3", ["4"]),
    ("4", [])
]

# Capacity of each link (Conjugated to Graph with order)
# Here all the 19 links have the same capacity
capacity = [45+8.4828, 40+7.6246, 70+0.0001, 40+6.5432, 45+7.4799]

# Free travel time of each link (Conjugated to Graph with order)
free_time = [
    4, 6, 2, 5, 3
]

# Origin-destination pairs
origins = ["1"]
destinations = ["4"]
# Generated ordered OD pairs: 
# first ("5", "15"), second ("5", "17"), third ("6", "15")...


# Demand between each OD pair (Conjugated to the Cartesian 
# product of Origins and destinations with order)
demand = [180]

