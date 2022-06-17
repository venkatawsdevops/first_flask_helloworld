from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'
@appx.route('/f')
def first():
     return 'first example'

if __name__ == '__main__':
    app.run()
