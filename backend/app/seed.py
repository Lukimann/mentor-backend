# backend/app/seed.py

from app import app, db
from app.models import User

with app.app_context():
    db.create_all()  # Create tables for all models

    # Check if the user already exists to avoid duplications
    if not User.query.filter_by(username='admin').first():
        # Add a sample user
        user = User(username='admin', email='admin@example.com')
        db.session.add(user)
        db.session.commit()

        print("Database seeded!")
    else:
        print("User already exists.")
