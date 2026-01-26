def test_homepage(client):
    """Test that the homepage loads successfully."""
    response = client.get('/')
    assert response.status_code == 200
    assert b'Work Tracker' in response.data

def test_add_worklog_entry(client):
    """Test adding a new work log entry."""
    response = client.post('/add', data={
        'pbi_number': 'TEST-001',
        'description': 'Test work item',
        'sprint': 'Sprint 1',
        'effort': '5',
        'comments': 'Test comments'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'TEST-001' in response.data

def test_add_achievement(client):
    """Test adding a new achievement."""
    response = client.post('/achievements/add', data={
        'title': 'Test Achievement',
        'description': 'Test accomplishment',
        'category': 'Technical',
        'sprint': 'Sprint 1',
        'column': 'Test comments'
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Test Achievement' in response.data

def test_delete_worklog_entry(client, init_database):
    """Test deleting a work log entry."""
    worklog, _ = init_database
    response = client.get(f'/delete/{worklog.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'TEST-001' not in response.data

def test_delete_achievement(client, init_database):
    """Test deleting an achievement."""
    _, achievement = init_database
    response = client.get(f'/achievements/delete/{achievement.id}', follow_redirects=True)
    assert response.status_code == 200
    assert b'Test Achievement' not in response.data

def test_worklog_model(init_database):
    """Test WorkLog model creation and attributes."""
    worklog, _ = init_database
    assert worklog.pbi_number == 'TEST-001'
    assert worklog.description == 'Test work item'
    assert worklog.sprint == 'Sprint 1'
    assert worklog.effort == 5
    assert worklog.comments == 'Test comments'

def test_achievement_model(init_database):
    """Test Achievement model creation and attributes."""
    _, achievement = init_database
    assert achievement.title == 'Test Achievement'
    assert achievement.description == 'Test accomplishment'
    assert achievement.category == 'Technical'
    assert achievement.sprint == 'Sprint 1'

def test_worklog_achievement_relationship(client, init_database):
    """Test relationship between WorkLog and Achievement."""
    worklog, _ = init_database

    # Add achievement linked to worklog
    response = client.post('/achievements/add', data={
        'title': 'Linked Achievement',
        'description': 'Achievement linked to worklog',
        'category': 'Technical',
        'sprint': 'Sprint 1',
        'worklog_id': str(worklog.id)
    }, follow_redirects=True)

    assert response.status_code == 200
    assert b'Linked Achievement' in response.data
    assert b'TEST-001' in response.data
