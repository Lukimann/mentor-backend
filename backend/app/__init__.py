from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'  # Replace with your PostgreSQL database URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()

# Import routes after initializing db to avoid circular imports
from backend.app import routes
