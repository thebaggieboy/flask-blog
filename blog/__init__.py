import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)

app.config['SECRET_KEY'] = '50d86ec193def31d8d172e2d2685f6dc'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://otkmfjuqnhzdzw:51fa9452c29b490f554b1ae1188e1a479b752308248ca7548aab5e001c9a3094@ec2-52-206-182-219.compute-1.amazonaws.com:5432/db0a9m697iqb0j'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from blog import routes
