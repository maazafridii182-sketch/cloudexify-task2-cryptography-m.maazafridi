import bcrypt
import json
import os

class SecureAuth:
    def __init__(self, db_file='users.json'):
        self.db_file = db_file
        self.users = self.load_users()

    def load_users(self):
        if os.path.exists(self.db_file):
            with open(self.db_file, 'r') as f:
                return json.load(f)
        return {}

    def save_users(self):
        with open(self.db_file, 'w') as f:
            json.dump(self.users, f)

    def register(self, username, password):
        if username in self.users:
            return "User exists!"
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        self.users[username] = hashed.decode()
        self.save_users()
        return "Registration successful!"

    def login(self, username, password):
        if username not in self.users:
            return False
        stored_hash = self.users[username].encode()
        return bcrypt.checkpw(password.encode('utf-8'), stored_hash)


auth = SecureAuth()
print(auth.register("alice", "SecurePass123"))

if auth.login("alice", "SecurePass123"):
    print("Login successful!")
else:
    print("Invalid credentials!")

print(auth.register("alice", "SecurePass123"))
