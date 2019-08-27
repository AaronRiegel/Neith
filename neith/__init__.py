from flask import Flask
from neith.setup import user, pw, ip, secret, db_name
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://{user}:{pw}@{ip}/{db_name}'
app.config['SECRET_KEY'] = secret
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from neith import routes
from neith import forms
