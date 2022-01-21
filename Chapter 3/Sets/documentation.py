vowels = {'a','e','e','i','o','u','u'}
# other way to define it 
# vowels = set('aeeiouu')

# >>> vowels = set('aeeiouu')
# >>> word = "hello"
# >>> u = vowels.union(set(word))
# untuk gabungin
# >>> u
# {'a', 'i', 'h', 'e', 'l', 'u', 'o'}
# >>> d = vowels.difference(set(word))
# cari yang beda
# >>> d
# {'a', 'i', 'u'}
# >>> i = vowels.intersection(set(word))
# cari yang sama
# >>> i
# {'e', 'o'}