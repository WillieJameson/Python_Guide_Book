paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)

for char in letters[0:6]:
  # '\t' is for 
  print('\t', char)
print()
for char in letters[-7:]:
  print('\t'*2, char)
print()
for char in letters[12:20]:
  print('\t'*3, char)

