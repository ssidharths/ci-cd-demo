import pytest
import sys
import os

# Ensure we can import from the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

# Now import the Flask app
try:
    from app import app
except ImportError as e:
    print(f"Import error: {e}")
    # Fallback: try different import methods
    import sys
    sys.path.append('..')
    from app import app

def test_app_is_working():
    """Test that the Flask app returns the correct response"""
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Server is running ..." in response.data

def test_app_exists():
    """Test that the app object exists"""
    assert app is not None
    assert app.name == 'app'

if __name__ == "__main__":
    # Allow running the test directly
    test_app_is_working()
    test_app_exists()
    print("All tests passed!")
