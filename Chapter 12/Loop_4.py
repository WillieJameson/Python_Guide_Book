from pprint import pprint
from datetime import datetime

def convert2ampm(time24:str) -> str:
  return datetime.strptime(time24, '%H:%M').strftime("%I,%M%p")

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

flight2 = {}

for k,v in flight.items():
  flight2[convert2ampm(k)] = v.title()

pprint(flight2)
