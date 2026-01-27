"""Flask app factory and extension setup for Work Log project."""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_name=None):
    """Application factory function."""
    flask_app = Flask(__name__)

    # Register blueprints
    from app.routes.main import main
    flask_app.register_blueprint(main)

    # Configuration
    if config_name == 'test':
        flask_app.config['TESTING'] = True
        flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        # Use PostgreSQL from environment variable, fallback to SQLite for local dev
        db_url = os.getenv('DATABASE_URL')
        if db_url:
            flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_url
        else:
            # Fallback to SQLite for local development
            flask_app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worklog.db'

    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(flask_app)
    migrate.init_app(flask_app, db)

    return flask_app

# Create the app instance for development
app = create_app()
