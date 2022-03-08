from flask import Flask, render_template, request, redirect, escape
# from vsearch import search4letters

from DBcm import UseDatabase

app = Flask(__name__)
app.config['dbconfig'] = {'host':'127.0.0.1', 
                          'user':'vsearch',
                          'password': 'vsearchpasswd',
                          'database':'vsearchlogDB',}

def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    """Return a set of the 'letter' found in 'phrase'"""
    return set(letters).intersection(set(phrase))

def log_request(req: 'flask_request', res:str) -> None:
    """Log details of the web request and the results."""

    with UseDatabase(app.config['dbconfig']) as cursor:

        _SQL = """insert into log
            (phrase, letters, ip, browser_string, results)
            values
            (%s, %s, %s, %s, %s)"""

        cursor.execute(_SQL,( req.form['phrase'],
                                req.form['letters'],
                                req.remote_addr,
                                req.user_agent.browser,
                                res,))
  

@app.route('/')
@app.route('/entry')
def entry_page() -> 'HTML':
    return render_template('entry.html', the_title='Welcome to search4letters on the web!')

@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    title = "Here are your results:"
    result = str(search4letters(phrase, letters))
    log_request(request, result)
    return render_template('results.html', the_title=title, the_phrase=phrase, the_letters=letters, the_results=result) 

@app.route('/viewlog')
def view_log() -> 'html':
    """Display the contents of the log file as HTML Table"""
    with UseDatabase(app.config['dbconfig']) as cursor:
         _SQL = """select phrase, letters, ip, browser_string, results from log"""
         cursor.execute(_SQL)
         contents = cursor.fetchall()

    titles = ('Phrase','Letters', 'Remote_addr', 'User_agent', 'Results')
    return render_template('viewlog.html',the_title='View log', the_row_titles=titles,the_data = contents)

if __name__ == '__main__':
    app.run(debug=True)


# @app.route('/test')
# def test():
#   return app
