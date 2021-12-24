from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/challenge_2.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

class Images(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    pathfile = db.Column(db.String(100), unique=True)
    type_image = db.Column(db.String(100))
    create_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
