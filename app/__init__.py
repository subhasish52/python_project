# Import necessary modules and classes
from flask import Flask  # Flask class for creating the Flask application instance
from flask_sqlalchemy import SQLAlchemy  # SQLAlchemy class for database operations
from flask_migrate import Migrate  # Migrate class for handling database migrations
from app.configisi import Config  # Config class for configuration settings

# Initialize SQLAlchemy and Migrate instances
db = SQLAlchemy()  # Initialize a SQLAlchemy object for database interactions
migrate = Migrate()  # Initialize a Migrate object for handling database migrations

def create_app():
    """
    Factory function to create and configure the Flask application instance.
    """
    app = Flask(__name__)  # Create the Flask application instance
    app.config.from_object(Config)  # Load configuration settings from the Config class

    db.init_app(app)  # Initialize the SQLAlchemy instance with the Flask app
    migrate.init_app(app, db)  # Initialize the Migrate instance with the Flask app and SQLAlchemy db

    # Register the blueprint for employee routes
    from .routes import employee_bp  # Import the blueprint for employee routes
    app.register_blueprint(employee_bp)  # Register the blueprint with the Flask app

    return app  # Return the configured Flask application instance
