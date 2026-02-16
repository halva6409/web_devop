from flask import Flask , jsonify

app = Flask(__name__)

@app.route('/')
def strt():
    stroks = [{'id': 1, 'title': 'First STR', 'source': 'STR'},
              {'id': 2 , 'title': 'Second str', 'source': 'str'}]
    return jsonify(stroks)

@app.route('/api/<int:news_id>')
def get_news_by_id(news_id):
    news = {'id': news_id, 'title': f'News {news_id}', 'source': news_id}
    return jsonify(news)

if __name__ == '__main__':
    app.run(debug=True)