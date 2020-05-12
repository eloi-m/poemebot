from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config['SECRET_KEY'] = "justarandomsecretkeypassingby"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Poem_database(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(100))
    title = db.Column(db.String(100))
    content = db.Column(db.UnicodeText)
    tweeted = db.Column(db.Boolean, default=False)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Poem {self.id}, author {self.author}, title {self.title}. Tweeted : {self.tweeted}>"
