import logging
from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from backend.app.models import db  # Import the db instance
from backend.app.routes import bp  # Import the blueprint

# Configure logging
logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost:5432/database_name'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY_HERE'  # Replace with a secret key for session management

# Initialize SQLAlchemy with the app
db.init_app(app)
migrate = Migrate(app, db)
CORS(app)  # Enable CORS for all routes

# Register the blueprint
app.register_blueprint(bp)

# Error handler for 404 (Page Not Found)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

# Error handler for other exceptions
@app.errorhandler(Exception)
def handle_exception(e):
    app.logger.error(f"An error occurred: {str(e)}", exc_info=True)
    return jsonify(message="An internal error occurred"), 500

with app.app_context():
    app.logger.debug("App context initialized.")
    print("Registered routes:")
    for rule in app.url_map.iter_rules():
        print(rule)
        app.logger.debug(f"Registered route: {rule}")

if __name__ == '__main__':
    app.logger.debug("Starting Flask server...")
    app.run(debug=True, host='0.0.0.0', port=5000)
