from database import db
import uuid
from sqlalchemy.orm import validates
class User(db.Model):
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    username = db.Column(db.String(80))
    email = db.Column(db.String(120), unique=True)
    password = db.Column(db.Text())

    @validates('password')
    def validate_password(self, key, password):
            if len(password) < 8:
                raise ValueError('Password must be at least 8 characters long.')
            return password
    def __init__(self, username, email , password):
        self.username = username
        self.email = email
        self.password= password

    def __repr__(self):
        return '<User %r>' % self.username