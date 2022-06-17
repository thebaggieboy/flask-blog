import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '50d86ec193def31d8d172e2d2685f6dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:// postgres://xucihjpazrnfax:d353a7cf4ca58fd1e3e95a5f1276ff898e9d11fc5c679923ca3df1cf94cda913@ec2-34-198-186-145.compute-1.amazonaws.com:5432/dd0ll6fks9f1g7'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from blog import routes
