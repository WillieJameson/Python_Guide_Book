letters_string = "Don't Panic!"

letters = list(letters_string)



print(letters)
## expected output = ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']

## letters[start:stop:step]

print(letters[0:10:3])
## Every third letter 
## expected output = ['D', "'", 'p', 'i']

print(letters[3:])
## Skip the first three letters
## expected output = ["'", 't', ' ', 'p', 'a', 'n', 'i', 'c', '!']

print(letters[:10])
## All the letters up to index 10 but not including index 10
## expected output = ['D', 'o', 'n', "'", 't', ' ', 'p', 'a', 'n', 'i']

print(letters[::2])
## Every second letter
## expected output = ['D', 'n', 't', 'p', 'n', 'c']