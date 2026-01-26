# Work Tracker

A Flask-based web application for tracking work logs and achievements, designed for performance review preparation and cross-device synchronization.

## Features

### 📋 Work Log

- Track daily work items with PBI numbers
- Record descriptions, sprints, and effort estimates
- Add comments and notes
- Easy deletion of completed items

### 🏆 Achievements

- Document accomplishments for performance reviews
- Categorize achievements (Technical, Leadership, Impact, etc.)
- Link achievements to specific work log entries
- Beautiful card-based layout for quick scanning
- Track sprints and add detailed comments

### 🔄 Cross-Device Sync

- PostgreSQL cloud database (Neon.tech)
- Access your data from any laptop
- No manual sync required
- Secure and reliable

## Quick Start

1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   cd Work-Tracker
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv worklog
   worklog\Scripts\activate  # On Windows
   source worklog/bin/activate   # On macOS/Linux
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Configure database (see [Setup Guide](.github/SETUP.md)):
   - Create free account at [neon.tech](https://neon.tech)
   - Copy `config/.env.example` to `.env`
   - Add your database connection string
5. Initialize database:

   ```bash
   flask db init
   flask db migrate -m "Initial migration"
   flask db upgrade
   ```

6. Run the app:

   ```bash
   python -m app
   ```

7. Open in browser: `http://127.0.0.1:5000`

## Documentation

- [Detailed Setup Guide](.github/SETUP.md) - Comprehensive setup instructions
- [Automation Scripts](.github/AUTOMATION.md) - Automated setup
- [Implementation Details](docs/IMPLEMENTATION.md) - Complete implementation summary and deployment

## Project Structure

```
Work-Tracker/
├── app/                    # Flask application
│   ├── models/            # Database models
│   ├── routes/            # Route handlers
│   ├── templates/         # Jinja2 templates
│   └── static/            # CSS, JS, images
├── config/                # Configuration files
│   └── .env.example       # Environment template
├── scripts/               # Setup and automation scripts
│   ├── setup-database.ps1 # Windows database setup
│   └── setup-database.sh  # Linux/macOS database setup
├── docs/                  # Documentation
│   └── IMPLEMENTATION.md  # Implementation details
├── migrations/            # Database migrations
├── tests/                 # Test files
├── .env                   # Local environment (not committed)
├── .github/               # GitHub-specific files
└── requirements.txt       # Python dependencies
```

## Configuration

- Database configuration via `.env` file (never committed to Git)
- Automatic fallback to SQLite for local development
- Cross-device sync through cloud PostgreSQL database

## Planned Improvements

- User authentication and authorization
- Edit functionality for work logs and achievements
- Search and filter capabilities
- Data export (CSV/PDF/Word)
- Dashboard and analytics
- Tags customization
- API endpoints

## Python Version

- Requires Python 3.8 or newer.

## License

MIT License. See `LICENSE` file for details.

## 🤖 Automation & Code Review

This project includes automated code review and CI/CD pipelines to ensure code quality.

### Local Code Review

Before committing, the pre-commit hook automatically runs:
- ✅ Unit tests
- ✅ Code linting (pylint)
- ✅ TODO/FIXME comment detection
- ✅ Large file detection

**Manual Code Review:**
```bash
# Linux/Mac
./scripts/code-review.sh

# Windows
scripts\code-review.bat
```

### CI/CD Pipeline

GitHub Actions automatically:
- 🧪 Runs tests on every push/PR
- 🔍 Performs code quality checks
- 🚀 Creates pull requests for feature branches
- 📊 Generates coverage reports

**Pre-commit Hook:**
The `.git/hooks/pre-commit` script runs automatically before each commit to ensure code quality.

**Automatic PR Creation:**
When you push a feature branch, GitHub Actions will automatically create a pull request with:
- ✅ CI status checks
- 📋 Code review checklist
- 🏷️ Automated labels

## Contributing

- Add docstrings to all new functions and classes.
- Write tests for new features.
- Follow Flask and Python best practices for structure and security.

## Running Tests

To run the test suite:

```bash
pytest
```

## Database Migrations

This project uses [Flask-Migrate](https://flask-migrate.readthedocs.io/) to manage database schema changes. Migration scripts are included in the `migrations/` folder. To apply migrations, run:

```bash
flask db upgrade
```

## Notes

- The database file `worklog.db` will be created automatically on first run (SQLite fallback).
- For production, use PostgreSQL via the `DATABASE_URL` environment variable.
