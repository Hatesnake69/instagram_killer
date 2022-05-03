from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


from .config import UPLOAD_FOLDER


app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
db = SQLAlchemy(app)
manager = LoginManager(app)
app.secret_key = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

app.debug = True


from app import views, models

db.create_all()
