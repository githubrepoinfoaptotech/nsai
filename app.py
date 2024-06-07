from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
from dbConfig import dbconnect
from database import db
app.config.from_object(dbconnect.Config)
db.init_app(app)

from api.user_api_routes import user_route
with app.app_context():
    from model.User import User
    db.create_all()
    db.session.commit()
# db = SQLAlchemy(app)
app.register_blueprint(user_route)
if __name__ == '__main__':
    app.run(debug=True,port=8080)
