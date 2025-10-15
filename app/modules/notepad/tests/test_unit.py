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

    
def test_notepad_create(test_client):
    """
    Tests the notepad can be created and saved to database correctly
    """
    with test_client.application.app_context():
        user = User.query.filter_by(email="user@example.com").first()
        notepad = Notepad(title="TestNotepad", body="This is a test.", user_id=user.id)
        db.session.add(notepad)
        db.session.commit()

        fetched = Notepad.query.filter_by(title="TestNotepad").first()
        assert fetched is not None
        assert fetched.body == "This is a test."
