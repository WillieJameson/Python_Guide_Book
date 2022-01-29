import re
from flask import Flask, render_template, request, redirect
# from vsearch import search4letters

def search4letters(phrase:str,letters:str='aeiou') -> set:
  """Return a set of the 'letter' found in 'phrase'"""
  return set(letters).intersection(set(phrase))

app = Flask(__name__)


@app.route('/')
@app.route('/entry')
def entry_page()-> 'HTML':
 return render_template('entry.html',the_title='Welcome to search4letters on the web!')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
  phrase = request.form['phrase']
  letters = request.form['letters']
  title = "Here are your results:"
  result = str(search4letters(phrase,letters))
  return render_template('results.html', the_title=title, the_phrase = phrase, the_letters = letters, the_results= result)


if __name__ == '__main__':
  app.run(debug=True)

# @app.route('/test')
# def test():
#   return app

