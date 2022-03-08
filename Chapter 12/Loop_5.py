from pprint import pp, pprint
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

fts = {convert2ampm(k): v.title() for k, v in flight.items()}

# when = {}
# for dest in set(fts.values()):
#   when[dest] = [k for k,v in fts.items() if v == dest ]

# compress
when = {dest : [k for k,v in fts.items() if v == dest] for dest in set(fts.values())}

pprint(when)




