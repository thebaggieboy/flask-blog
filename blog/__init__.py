import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '50d86ec193def31d8d172e2d2685f6dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://lwpvzjmgdtrjgb:22a188a7e6041a788bc732ce7d4c7dba606785de7b6f7796cf7a9274050db1e3@ec2-34-227-120-79.compute-1.amazonaws.com:5432/d9eoe35v7ucfdn'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from blog import routes
