from flask import Flask
# from vsearch import search4letters

def search4letters(phrase:str,letters:str='aeiou') -> set:
  """Return a set of the 'letter' found in 'phrase'"""
  return set(letters).intersection(set(phrase))

app = Flask(__name__)

@app.route('/')
def hello() -> str:
  return "hello world from flask"

@app.route('/search4')
def do_search() -> str:
  return str(search4letters('life,the universe, and everthing','eiru,'))


app.run()