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
    app = Flask(__name__)

    # Configuration
    if config_name == 'testing':
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    else:
        # Use PostgreSQL from environment variable, fallback to SQLite for local dev
        database_url = os.getenv('DATABASE_URL')
        if database_url:
            app.config['SQLALCHEMY_DATABASE_URI'] = database_url
        else:
            # Fallback to SQLite for local development
            app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///worklog.db'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register blueprints
    from app.routes.main import main
    app.register_blueprint(main)

    return app

# Create the app instance for development
app = create_app()
