import csv

with open('buzzers.csv') as data:
  """read the data a line at a time with “csv.reader”."""
  for line in csv.reader(data):
    print(line)

# ['TIME', 'DESTINATION ']
# ['09:35', 'FREEPORT ']
# ['17:00', 'FREEPORT ']
# ['09:55', 'WEST END ']
# ['19:00', 'WEST END ']
# ['10:45', 'TREASURE CAY ']
# ['12:00', 'TREASURE CAY ']
# ['11:45', 'ROCK SOUND ']
# ['17:55', 'ROCK SOUND']