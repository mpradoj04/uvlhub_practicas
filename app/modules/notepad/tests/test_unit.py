import pytest

from app import db
from app.modules.auth.models import User
from app.modules.conftest import login, logout
from app.modules.notepad.models import Notepad

    
@pytest.fixture(scope='module')
def test_client(test_client):
    
    with test_client.application.app_context():
        user_test = User(email="user@example.com", password="test1234")
        db.session.add(user_test)
        db.session.commit()
        
    yield test_client


def test_list_empty_notepad_get(test_client):
    """
    Tests access to the empty notepad list via GET request.
    """
    login_response = login(test_client, "user@example.com", "test1234")
    assert login_response.status_code == 200, "Login was unsuccessful."

    response = test_client.get("/notepad")
    assert response.status_code == 200, "The notepad page could not be accessed."
    assert b"You have no notepads." in response.data, "The expected content is not present on the page"

    logout(test_client)
