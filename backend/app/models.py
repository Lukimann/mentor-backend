from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Volunteer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.String(100))
    occupation = db.Column(db.String(100))
    country = db.Column(db.String(100))
    days = db.Column(db.String(100))
    times = db.Column(db.String(100))
    motivation = db.Column(db.Text)

    def __repr__(self):
        return f'<Volunteer {self.name}>'

class NewsletterSubscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    
    def __repr__(self):
        return f'<NewsletterSubscriber {self.email}>'

class Contacts(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text)

    def __repr__(self):
        return f'<Contacts {self.name}>'
