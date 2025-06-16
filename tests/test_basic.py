from app import app

def test_homepage():
    """Test that the homepage loads successfully."""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b'Work Log' in response.data
