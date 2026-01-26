# Work Tracker Setup Guide

This guide will help you set up the Work Tracker application with PostgreSQL database for cross-laptop synchronization.

## Prerequisites

- Python 3.8 or higher
- Git
- A Neon.tech account (free tier is sufficient)

## Initial Setup (First Time)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd Work-Tracker
```

### 2. Set Up Python Virtual Environment

```bash
# Create virtual environment
python -m venv worklog

# Activate virtual environment
# On Windows:
worklog\Scripts\activate
# On macOS/Linux:
source worklog/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up PostgreSQL Database (Neon.tech)

1. Go to [neon.tech](https://neon.tech) and sign up for a free account
2. Create a new project (name it "work-tracker" or similar)
3. Copy your connection string (it looks like):
   ```
   postgresql://username:password@hostname.neon.tech/database?sslmode=require
   ```

### 5. Configure Environment Variables

1. Copy the example environment file:

   ```bash
   cp config/.env.example .env
   ```

2. Edit `.env` and add your Neon.tech connection string:
   ```
   DATABASE_URL=postgresql://your-username:your-password@your-hostname.neon.tech/your-database?sslmode=require
   ```

### 6. Initialize Database

```bash
# Initialize migrations
flask db init

# Create initial migration
flask db migrate -m "Initial migration with WorkLog and Achievement models"

# Apply migrations to database
flask db upgrade
```

### 7. Run the Application

```bash
python -m app
```

The application will be available at: `http://127.0.0.1:5000`

## Setup on Additional Laptops

### 1. Clone and Install

```bash
git clone <your-repo-url>
cd Work-Tracker
python -m venv worklog
worklog\Scripts\activate  # On Windows
pip install -r requirements.txt
```

### 2. Add Environment Variables

Create a `.env` file with the **SAME** database connection string:

```
DATABASE_URL=postgresql://your-username:your-password@your-hostname.neon.tech/your-database?sslmode=require
```

### 3. Run the Application

```bash
python -m app
```

That's it! Your data will be automatically synchronized through the cloud database.

## Development Workflow

### Adding New Features

1. Make changes to your code
2. If you modified models, create a migration:
   ```bash
   flask db migrate -m "Description of changes"
   flask db upgrade
   ```
3. Commit and push changes to Git:
   ```bash
   git add .
   git commit -m "Your commit message"
   git push
   ```

### Syncing Between Laptops

1. Pull latest code:
   ```bash
   git pull
   ```
2. Apply any new migrations:
   ```bash
   flask db upgrade
   ```
3. Run the app:
   ```bash
   python -m app
   ```

## Using the Application

### Work Log Tab

- Track your daily work items with PBI numbers, descriptions, sprints, and effort points
- Click "Add Work Log Entry" to create new entries
- Delete entries you no longer need

### Achievements Tab

- Document accomplishments for performance reviews
- Add title, description, category, and comments
- Link achievements to specific work log entries
- Organized in a card-based layout for easy scanning

## Troubleshooting

### Database Connection Issues

If you get database connection errors:

1. Check that your `.env` file exists and contains the correct `DATABASE_URL`
2. Verify your Neon.tech database is active (free tier may pause after inactivity)
3. Check your internet connection

### Migration Issues

If migrations fail:

```bash
# Reset migrations (WARNING: This will delete all data)
flask db downgrade
flask db upgrade
```

### Local Development Without Cloud Database

If you want to work offline, comment out the `DATABASE_URL` in `.env`:

```
# DATABASE_URL=postgresql://...
```

The app will automatically fall back to SQLite (local database).

## Security Notes

- **Never commit your `.env` file** - it's already in `.gitignore`
- Share your database connection string securely (not via public channels)
- Consider making your GitHub repository private if it contains sensitive project information
- For production use, enable authentication (to be added in future updates)

## Additional Resources

- [Neon.tech Documentation](https://neon.tech/docs)
- [Flask-SQLAlchemy Documentation](https://flask-sqlalchemy.palletsprojects.com/)
- [Flask-Migrate Documentation](https://flask-migrate.readthedocs.io/)
