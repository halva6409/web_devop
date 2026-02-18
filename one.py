from flask import Flask, render_template, jsonify
import os

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder = os.path.join(basedir, 'templates'),
            static_folder = os.path.join(basedir, 'static'))

@app.route('/')
def start():
    news = [
        {'id': 1, 'title': 'Запуск нового iPhone 16', 'source': 'BBC'},
        {'id': 2, 'title': 'Tesla представила новую модель', 'source': 'Reuters'},
        {'id': 3, 'title': 'Биткоин достиг $100,000', 'source': 'CNN'},
        {'id': 4, 'title': 'SpaceX успешно запустила ракету', 'source': 'BBC'}
    ]
    return jsonify(news)

@app.route('/news')
def new():
    # ДОБАВЬ ЭТИ НОВОСТИ
    news_list = [
        {'id': 1, 'title': 'Запуск нового iPhone 16', 'source': 'BBC'},
        {'id': 2, 'title': 'Tesla представила новую модель', 'source': 'Reuters'},
        {'id': 3, 'title': 'Биткоин достиг $100,000', 'source': 'CNN'},
        {'id': 4, 'title': 'SpaceX успешно запустила ракету', 'source': 'BBC'}
    ]
    # Передай в шаблон
    return render_template('index.html', news=news_list)


if __name__ == '__main__':
    app.run(debug = True, port = 7777)