destinations = []
for dest in flights.values():
  destinations.append(dest.title())

# compress
# make a list 
more_dest =[]

# iterate through each of the destinations
  # more_dest= [for dest in flights.values() ]

# Append the converted data to the new list,
more_dest= [dest.title() for dest in flights.values()]