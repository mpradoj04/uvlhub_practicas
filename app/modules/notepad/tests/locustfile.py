from locust import HttpUser, TaskSet, task, between
from core.environment.host import get_host_for_locust_testing


class NotepadBehavior(TaskSet):
    def on_start(self):
        self.login()
        self.index()
        
    def login(self):
        response = self.client.post(
            "/login",
            json={"email": "user@example.com", "password": "test1234"}
        )
        if response.status_code == 200:
            print("User logged.")
        else:
            print(f"Login failed: {response.status_code}")

    @task(2)
    def index(self):
        response = self.client.get("/notepad")

        if response.status_code == 200:
            print("Notepads retrieved succesfully.")
        else:
            print(f"Notepad index failed: {response.status_code}")
            
    @task(1)
    def create_notepad(self):
        notepad = {
            "title": "TestNotepad",
            "body": "This is a test."
        }
        response = self.client.post("/notepad/create", data=notepad)
        
        if response.status_code == 200:
            print("Notepad created successfully.")
        else:
            print(f"Error while creating notepad: {response.status_code}")


class NotepadUser(HttpUser):
    tasks = [NotepadBehavior]
    wait_time = between(5, 9)
    host = get_host_for_locust_testing()
