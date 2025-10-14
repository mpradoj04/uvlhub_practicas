from core.seeders.BaseSeeder import BaseSeeder
from app.modules.auth.models import User
from models import Notepad


class NotepadSeeder(BaseSeeder):

    def run(self):
        
        # Retrieve user
        user = User.query.filter_by(email="user1@example.com").first()
            
        if not user:
            raise Exception("User not found. Please seed users first.")

        data = [
            Notepad(
                title="Notepad_Test1",
                body="This is a test notepad",
                user_id=user.id
            ),
            Notepad(
                title="Notepad_Test2",
                body="This is a test notepad",
                user_id=user.id
            )
            
        ]

        self.seed(data)
