from flask import Flask, render_template, jsonify
import os
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__,
            template_folder = os.path.join(basedir, 'templates'),
            static_folder = os.path.join(basedir, 'static'))

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///news.db'
db = SQLAlchemy(app)

class Mews(db.Model):
    id       = db.Column(db.Integer , primary_key = True)         
    title    = db.Column(db.String(200), nullable = False)           
    source   = db.Column(db.String(100))            
    content  = db.Column(db.Text)             
    date_new = db.Column(db.DateTime, default = datetime.now)              

@app.route('/api/news')
def start():
    news = [
        {'id': 1, 'title': 'Запуск нового iPhone 16', 'source': 'BBC'},
        {'id': 2, 'title': 'Tesla представила новую модель', 'source': 'Reuters'},
        {'id': 3, 'title': 'Биткоин достиг $100,000', 'source': 'CNN'},
        {'id': 4, 'title': 'SpaceX успешно запустила ракету', 'source': 'BBC'}
    ]
    return jsonify(news)

@app.route('/')
def new():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True, port = 7777)