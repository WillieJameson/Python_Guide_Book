import csv

with open('buzzers.csv') as data:
  for line in csv.DictReader(data):
    print(line)

# {'TIME': '09:35', 'DESTINATION ': 'FREEPORT '}
# {'TIME': '17:00', 'DESTINATION ': 'FREEPORT '}
# {'TIME': '09:55', 'DESTINATION ': 'WEST END '}
# {'TIME': '19:00', 'DESTINATION ': 'WEST END '}
# {'TIME': '10:45', 'DESTINATION ': 'TREASURE CAY '}
# {'TIME': '12:00', 'DESTINATION ': 'TREASURE CAY '}
# {'TIME': '11:45', 'DESTINATION ': 'ROCK SOUND '}
# {'TIME': '17:55', 'DESTINATION ': 'ROCK SOUND'}