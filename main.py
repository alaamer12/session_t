import uuid
from datetime import datetime, timedelta

class SessionManager:
    def __init__(self):
        self.sessions = {}

    def create_session(self, user_id):
        # Generate a unique session ID
        session_id = str(uuid.uuid4())
        # Set session expiration time
        expiration_time = datetime.now() + timedelta(minutes=SESSION_EXPIRATION_MINUTES)
        # Store session data
        self.sessions[session_id] = {'user_id': user_id, 'expiration_time': expiration_time}
        return session_id

    def get_session(self, session_id):
        session = self.sessions.get(session_id)
        if session and session['expiration_time'] > datetime.now():
            return session
        else:
            return None

    def update_session(self, session_id, user_id):
        if session_id in self.sessions:
            self.sessions[session_id]['user_id'] = user_id
            self.sessions[session_id]['expiration_time'] = datetime.now() + timedelta(minutes=SESSION_EXPIRATION_MINUTES)

    def delete_session(self, session_id):
        if session_id in self.sessions:
            del self.sessions[session_id]

# Example usage
SESSION_EXPIRATION_MINUTES = 30
session_manager = SessionManager()

# Create session for user 123
user_id = 123
session_id = session_manager.create_session(user_id)
print(f"Created session with ID: {session_id}")

# Retrieve session
session = session_manager.get_session(session_id)
if session:
    print(f"User ID in session: {session['user_id']}")
else:
    print("Session not found or expired")

# Update session
session_manager.update_session(session_id, 456)
session = session_manager.get_session(session_id)
if session:
    print(f"Updated user ID in session: {session['user_id']}")

# Delete session
session_manager.delete_session(session_id)
session = session_manager.get_session(session_id)
if not session:
    print("Session deleted")
