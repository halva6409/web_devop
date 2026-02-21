from flask import Flask, render_template, jsonify , request
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

@app.route('/api/news' , methods=['POST', 'GET'])
def start():
    if request.method == 'POST':
        data = request.json
        news_list = Mews(title=data['title'], source=data.get('source' , 'Unknown'), content=data.get('content', ''))
        db.session.add(news_list)
        db.session.commit()
        return jsonify({'id': news_list.id, 'message': 'Create'}), 201
    if request.method == 'GET':
        news_list = Mews.query.all()
        return jsonify([{
            'id': n.id,
            'title': n.title,
            'source': n.source,
            'content': n.content
        } for n in news_list])

@app.route('/')
def new():
    return render_template('index.html')

@app.route('/api/news/<int:id>', methods=['DELETE'])
def del_te(id):
    news = Mews.query.get(id)
    db.session.delete(news)
    db.session.commit()
    return '', 204


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True, port = 7777)