from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin):
    def __init__(self, id, username, password_hash):
        self.id = id
        self.username = username
        self.password_hash = password_hash

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)

# 하드코딩된 사용자 정보
users = {
    "1": User("1", "MNUScE", generate_password_hash("MNUScE"))
}

def get_user_by_username(username):
    for user in users.values():
        if user.username == username:
            return user
    return None
