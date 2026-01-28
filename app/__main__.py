"""Main entry point for running the Work Log Flask app."""
from app import create_app, db

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
