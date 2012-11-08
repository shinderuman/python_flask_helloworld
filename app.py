import os
from flask import Flask, session, redirect, url_for, escape, request, render_template
import MySQLdb
app = Flask(__name__)

@app.route('/')
def hello_world():
  return 'Hello World!'

@app.route('/world/<bar>')
def world(bar=None):
  return render_template('world.html', bar=bar)

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

@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    session['name'] = request.form['name']
    return redirect(url_for('session_check'))
  return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('name', None)
  return 'You are logouted'

@app.route('/session_check')
def session_check():
  if 'name' in session:
    return 'Your name is %s' % session['name']
  return "session['name'] is None"

app.secret_key = os.urandom(24)
if __name__ == '__main__':
  app.run(debug=True)

