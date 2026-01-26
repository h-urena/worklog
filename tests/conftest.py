import pytest
import os
from app import create_app, db

@pytest.fixture
def app():
    """Test app fixture with test database."""
    app = create_app('testing')
    return app

@pytest.fixture
def client(app):
    """Test client fixture."""
    return app.test_client()

@pytest.fixture(autouse=True)
def setup_database(app):
    """Set up database tables for all tests."""
    with app.app_context():
        db.create_all()
        yield
        db.drop_all()

@pytest.fixture
def init_database(app):
    """Initialize database with test data."""
    with app.app_context():
        from app.models.worklog import WorkLog
        from app.models.achievement import Achievement

        # Create test data
        worklog = WorkLog(
            pbi_number='TEST-001',
            description='Test work item',
            sprint='Sprint 1',
            effort=5,
            comments='Test comments'
        )
        db.session.add(worklog)

        achievement = Achievement(
            title='Test Achievement',
            description='Test accomplishment',
            category='Technical',
            sprint='Sprint 1'
        )
        db.session.add(achievement)
        db.session.commit()

        yield worklog, achievement

        # Cleanup
        db.session.remove()