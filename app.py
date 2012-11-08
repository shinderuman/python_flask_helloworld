from flask import Flask
import MySQLdb
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/world/<bar>')
def world(bar):
  return bar

@app.route('/db')
def db():
  connect = MySQLdb.connect(db='foo', host='127.0.0.1', port=3306, user='root', passwd='hoge')
  cur = connect.cursor()
  cur.execute('select text from bar')
  rows = cur.fetchall()
  str = ''
  for row in rows:
    str += row[0]
  cur.close()
  connect.close
  return str

if __name__ == '__main__':
  app.run(debug=True)
