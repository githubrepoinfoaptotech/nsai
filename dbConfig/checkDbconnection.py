from sqlalchemy.exc import OperationalError
from database import db
from sqlalchemy import text


def check_db_connection():
        try:
            # Attempt to execute a simple query
            db.session.execute(text('SELECT 1'))
        except OperationalError:
            # If an OperationalError occurs, close all connections and roll back the session
            db.session.remove()
            db.engine.dispose()
            db.session.rollback()
            # Optionally, re-establish the connection by executing a simple query
            try:
                db.session.execute(text('SELECT 1'))
            except OperationalError:
                # Handle the case where reconnection fails
                raise
