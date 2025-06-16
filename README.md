# Work Log Flask App

A simple Flask application to keep track of work log entries using SQLite.

## Features

- Add, view, and delete work log entries
- Each entry includes date, description, tags, and time spent

## Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/work-log-flask.git
   cd work-log-flask
   ```
2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv worklog
   .\worklog\Scripts\Activate  # On Windows
   source worklog/bin/activate   # On macOS/Linux
   ```
3. Install dependencies and run the app as described above.

## Configuration

- The default database is SQLite and will be created as `worklog.db` in the project root.
- To use a different database, set the `SQLALCHEMY_DATABASE_URI` in `app/__init__.py` or via environment variable.
- For production, set `FLASK_ENV=production` and configure a secure secret key.

## Planned Improvements

- Environment-based configuration
- Flask-Migrate integration
- CSRF protection and input validation
- More tests and coverage
- User authentication
- API endpoints
- Data export (CSV/PDF)
- Dashboard and analytics

## Python Version

- Requires Python 3.8 or newer.

## License

MIT License. See `LICENSE` file for details.

## Contact

For questions or suggestions, open an issue or contact [your email here].

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the app:
   ```bash
   python -m app
   ```

## Project Structure

- `app/` - Main application code
- `app/models/` - Database models
- `app/routes/` - Application routes
- `app/templates/` - HTML templates
- `app/static/` - CSS and static files
- `tests/` - (For your tests)

## Running Tests

To run the test suite:

```bash
pytest
```

## Contributing

- Add docstrings to all new functions and classes.
- Write tests for new features.
- Follow Flask and Python best practices for structure and security.

## Notes

- The database file `worklog.db` will be created automatically on first run.

## Database Migrations

This project uses [Flask-Migrate](https://flask-migrate.readthedocs.io/) to manage database schema changes. Migration scripts are included in the `migrations/` folder. To apply migrations, run:

```bash
flask db upgrade
```
