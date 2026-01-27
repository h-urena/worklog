"""
Pytest configuration and fixtures for the worklog application.
"""

import os.path
import sys
import pytest
from app import create_app, db
from app.models.achievement import Achievement
from app.models.worklog import WorkLog

# Add the project root to Python path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


@pytest.fixture
def test_app():
    """Test app fixture."""
    return create_app('test')


@pytest.fixture
def client(test_app):
    """Test client fixture."""
    return test_app.test_client()


@pytest.fixture(autouse=True)
def setup_database(test_app):
    """Set up database tables for all tests."""
    with test_app.app_context():
        db.create_all()
        yield
        db.drop_all()


@pytest.fixture
def init_database(test_app):
    """Initialize database with test data."""
    with test_app.app_context():
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
