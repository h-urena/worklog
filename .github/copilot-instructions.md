<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

This is a Flask + PostgreSQL work tracker project with two main features:
1. **Work Log**: Track daily work items (PBI numbers, descriptions, sprints, effort)
2. **Achievements**: Document accomplishments for performance reviews

## Architecture
- **Backend**: Flask with Blueprint pattern for route organization
- **Database**: PostgreSQL (via Neon.tech) for cross-device sync, SQLite fallback for local dev
- **ORM**: SQLAlchemy with Flask-Migrate for database migrations
- **Frontend**: Jinja2 templates with Tailwind CSS for styling
- **Tabs**: JavaScript-based tab switching between Work Log and Achievements views

## Key Models
- `WorkLog`: PBI tracking (pbi_number, description, sprint, effort, comments)
- `Achievement`: Accomplishment tracking (title, description, category, sprint, column, worklog_id foreign key)

## Environment Setup
- Use `.env` file for `DATABASE_URL` (never commit this file)
- Virtual environment in `worklog/` directory
- Dependencies managed via `requirements.txt`

## Best Practices
- Keep code modular using Flask blueprints
- Document all functions with docstrings
- Use SQLAlchemy ORM patterns (avoid raw SQL)
- Maintain responsive design with Tailwind CSS
- Follow RESTful routing conventions
- Create database migrations for all schema changes

## Development Workflow
1. Activate virtual environment: `worklog\Scripts\activate`
2. Make model changes → Create migration: `flask db migrate -m "description"`
3. Apply migration: `flask db upgrade`
4. Test locally before committing

## Future Enhancements
- Add user authentication
- Implement edit functionality for entries
- Add search/filter capabilities
- Export achievements to PDF/Word for reviews
