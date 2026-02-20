from main import app, db, Mews

with app.app_context():
    new1 = Mews(title = 'Первый iPhone', source = 'Apple', content = 'Первый в мире айфон')
    new2 = Mews(title='Tesla представила новую модель', source='Reuters', content='Подробности...')
    new3 = Mews(title='Биткоин достиг $100,000', source='CNN', content='Подробности...')

    db.session.add(new1)
    db.session.add(new2)
    db.session.add(new3)

    db.session.commit()