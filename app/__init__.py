from .config import UPLOAD_FOLDER

from flask import Flask


app = Flask(__name__, static_folder='static')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

from app import views