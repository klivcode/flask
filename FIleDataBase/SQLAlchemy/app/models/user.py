
from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

# db.create_all()
class User(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=True)
    email=db.Column(db.String(200), nullable=True)
    posts=db.relationship('post', backref='author', lazy=True)

#User.query.all(), .filter_by()