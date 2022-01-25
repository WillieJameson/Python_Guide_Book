def search4vowel(phrase:str) ->set:
  """Return any vowels found in a supplied word."""
  vowels = set('aeiou')
  # word = input('provide a word to search for vowel: ')
  found = vowels.intersection(set(phrase))
  return found

def search4letters(phrase:str,letters:str='aeiou') -> set:
  """Return a set of the 'letter' found in 'phrase'"""
  return set(letters).intersection(set(phrase))