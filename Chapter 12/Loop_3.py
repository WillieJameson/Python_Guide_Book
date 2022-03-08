from pprint import pprint


with open('buzzers.csv') as data:
  # ignore the header info
  ignore = data.readline() 
  flight = {}
  for line in data :
    """ strip is for remove the unwanted trailing newline from the raw data"""
    k,v = line.strip().split(',')
    flight[k] = v

  print(flight)

  pprint(flight)