from . import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(80), unique=True)
    user_library = db.Column(db.String(65535))
    follow_list = db.Column(db.String(65535))

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.TEXT(65535))
    chapters = db.Column(db.Integer)
    has_access = db.Column(db.String(65535))


class Annotation(db.Model):
    __tablename__ = "annotations"

    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey(Book.id), primary_true=True)
    text = db.Column(db.TEXT(65535))
