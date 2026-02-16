from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/news')
def get_news():
    news = [
        {'id': 1, 'title': 'First STR', 'source': 'STR'},
        {'id': 2, 'title': 'Second str', 'source': 'str'}
    ]
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)