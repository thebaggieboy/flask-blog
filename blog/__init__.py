import bcrypt
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_ckeditor import CKEditor


app = Flask(__name__)
ckeditor = CKEditor(app)

app.config['DEBUG']=True
app.config['SECRET_KEY'] = '50d86ec193def31d8d172e2d2685f6dc'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres.jegcscbydcktaescyhgn:eWgbVu63Q7VXr4uq@aws-0-us-east-1.pooler.supabase.com:6543/postgres"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)
migrate = Migrate(app, db)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
from blog import routes
