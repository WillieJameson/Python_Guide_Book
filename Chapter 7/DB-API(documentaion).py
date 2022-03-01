

dbconfig = {'host':'127.0.0.1', 
            'user':'vsearch',
            'password': 'vsearchpasswd',
            'database':'vsearchlogDB',}

import mysql.connector

conn = mysql.connector.connect(**dbconfig)

cursor = conn.cursor()

_SQL = """show tables"""
cursor.execute(_SQL)
# • cursor.fetchone retrieves a single row of results.
# • cursor.fetchmany retrieves the number of rows you specify.
# • cursor.fetchall retrieves all the rows that make up the results.
res = cursor.fetchall()
print(res)
"""[('log',)]"""

_SQL = """describe log"""
cursor.execute(_SQL)
res = cursor.fetchall()
print(res)
"""[('id', 'int(11)', 'NO', 'PRI', None, 'auto_increment'), ('ts', 'timestamp', 'NO', '', 'CURRENT_TIMESTAMP', ''), ('phrase', 'varchar(128)', 'NO', '', None, ''), ('letters', 'varchar(32)', 'NO', '', None, ''), ('ip', 'varchar(16)', 'NO', '', None, ''),('browser_string', 'varchar(256)', 'NO', '', None, ''), ('results', 'varchar(64)', 'NO', '', None, '')]"""

"""HardCode version which is not recommended"""
_SQL = """insert into log (phrase, letters, ip, browser_string, results) values ('hitch-hiker', 'aeiou', '127.0.0.1', 'Firefox', "{'e', 'i'}")"""
cursor.execute(_SQL)

"""recommended version"""
_SQL = """insert into log
(phrase, letters, ip, browser_string, results)
 values
(%s, %s, %s, %s, %s)"""
cursor.execute(_SQL, ('hitch-hiker', 'xyz', '127.0.0.1', 'Safari', 'set()'))

conn.commit()
_SQL = """select * from log"""
cursor.execute(_SQL)
for row in cursor.fetchall():
  print(row)


"""tidy UP"""

cursor.close()
conn.close()