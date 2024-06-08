from flask import Flask
from dbConfig import dbconnect
from database import db
from sqlalchemy.exc import OperationalError
from sqlalchemy import text
from flask_cors import CORS
from dbConfig import checkDbconnection

app = Flask(__name__)
app.config.from_object(dbconnect.Config)
db.init_app(app)

from api.user_api_routes import user_route
app.register_blueprint(user_route)
CORS(app, origins='*')

@app.before_request
def before_request():
    checkDbconnection.check_db_connection()

with app.app_context():
    from model.User import User
    db.create_all()
    db.session.commit()

# Remove the if __name__ == '__main__' block
# if __name__ == '__main__':
#     app.run(debug=True, port=8080)