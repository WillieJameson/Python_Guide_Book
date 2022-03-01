"""This is the code that we'd like to be able to write
in order to do the same thing as our current code (replacing the suite in the “log_request” function). But don't try to run this code yet, as it won't work without the “UseDatabase” context manager."""

import mysql.connector

def log_request(req: 'flask_request', res:str) -> None:
  dbconfig = {'host':'127.0.0.1', 
              'user':'vsearch',
              'password': 'vsearchpasswd',
              'database':'vsearchlogDB',}
  
  with UseDatabase(dbconfig) as cursor:

    _SQL = """insert into log
      (phrase, letters, ip, browser_string, results)
      values
      (%s, %s, %s, %s, %s)"""

    cursor.execute(_SQL,( req.form['phrase'],
                          req.form['letters'],
                          req.remote_addr,
                          req.user_agent.browser,
                          res,))
  