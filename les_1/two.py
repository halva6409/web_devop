from flask import Flask

app = Flask(__name__)

@app.route('/')
def hel():
    return 'Right'

@app.route('/abote')
def aboute():
    return 'страница aboute'

@app.route('/user/<name>')
def neme(name):
    return f"Hi , {name}"

if __name__ == '__main__':
    app.run(debug = True)