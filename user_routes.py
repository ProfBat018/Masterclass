from fastapi import FastAPI, Form
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

users = []

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = self.hash_password(password)

    def hash_password(self, password):
        return pwd_context.hash(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.password)


@app.post("/register")
def register(username: str = Form(...), password: str = Form(...)):
    # Check if user already exists
    for user in users:
        if user.username == username:
            return {"error": "User already exists"}

    # Create a new user and add to the list of users
    new_user = User(username, password)
    users.append(new_user)

    return {"username": new_user.username, "message": "User registered successfully"}


@app.post("/login")
def login(username: str = Form(...), password: str = Form(...)):
    # Find the user by username
    user = None
    for u in users:
        if u.username == username:
            user = u
            break

    if user is None:
        return {"error": "User not found"}

    # Verify the password
    if user.verify_password(password):
        return {"message": "Login successful"}
    else:
        return {"error": "Invalid password"}
