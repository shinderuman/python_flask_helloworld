from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/world')
def hello_world():
    return 'World!'

if __name__ == '__main__':
    app.run()
