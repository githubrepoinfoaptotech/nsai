from sqlalchemy.exc import OperationalError
from database import db
from sqlalchemy import text


def check_db_connection():
    try:
        # Attempt to execute a simple query
        db.session.execute(text('SELECT 1'))
    except OperationalError:
        # If an OperationalError occurs, roll back the session
        db.session.rollback()
