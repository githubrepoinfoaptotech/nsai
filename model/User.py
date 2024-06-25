from datetime import datetime

from database import db
from sqlalchemy import Column, String, Uuid
from uuid import uuid4
from sqlalchemy import event
from werkzeug.security import generate_password_hash
from sqlalchemy import Integer, String, DateTime,Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship


class User(db.Model):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(type_=Uuid, primary_key=True, default=uuid4)
    email: Mapped[str] = mapped_column(type_=String(250), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    fullname: Mapped[str] = mapped_column(type_=String(250), nullable=False)
    createdAt = mapped_column(type_=DateTime, default=datetime.utcnow)
    updatedAt = mapped_column(type_=DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "email": self.email,
            "password": self.password,
            "fullname": self.fullname
        }


@event.listens_for(User, "before_insert")
def hash_password(mapper, connect, target):
    if target.password:
        target.password = generate_password_hash(target.password, method="pbkdf2:sha256", salt_length=18)

