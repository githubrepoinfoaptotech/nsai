from flask import Flask
from dbConfig import dbconnect
from database import db
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
import threading
import time

app = Flask(__name__)
app.config.from_object(dbconnect.Config)
db.init_app(app)

from api.user_api_routes import user_route
app.register_blueprint(user_route)

def check_db_connection():
    try:
        with app.app_context():
            db.session.execute(text('SELECT 1'))
            db.session.commit()
        # print("Database connection is active.")
    except OperationalError as e:
        # print(f"Database connection lost. Reconnecting... Error: {e}")
        with app.app_context():
            db.session.rollback()
            db.session.expire_all()
            db.session.execute(text('SELECT 1'))
            db.session.commit()
        print("Database reconnected successfully.")
    # except Exception as e:
    #     print(f"An error occurred: {e}")

def check_db_thread():
    while True:
        check_db_connection()
        time.sleep(65)

if __name__ == '__main__':
    db_thread = threading.Thread(target=check_db_thread)
    db_thread.daemon = True
    db_thread.start()

    app.run(debug=True, port=8080)
