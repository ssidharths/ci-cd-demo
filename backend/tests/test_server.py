import os
import sys
import pytest

# Add the backend directory to Python path
backend_dir = os.path.dirname(os.path.abspath(__file__))
backend_parent = os.path.dirname(backend_dir)
if backend_parent not in sys.path:
    sys.path.insert(0, backend_parent)


# Test the import first
def test_can_import_app():
    """Test that we can import the Flask app"""
    try:
        from app import app
        assert app is not None
        print(f"✅ Successfully imported Flask app: {app}")
    except ImportError as e:
        pytest.fail(f"❌ Cannot import Flask app: {e}")


def test_flask_app_response():
    """Test that the Flask app returns correct response"""
    from app import app

    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200
        assert b"Server is running ..." in response.data
        print(f"✅ Flask app response: {response.data.decode()}")


def test_flask_app_configuration():
    """Test Flask app basic configuration"""
    from app import app

    assert app.name == 'app'
    assert hasattr(app, 'test_client')
    print("✅ Flask app configuration is correct")
