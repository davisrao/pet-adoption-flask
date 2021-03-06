"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet (db.Model):
    """
    Pet. Class for creating new adopted pet
    """
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                    primary_key=True,
                    autoincrement=True)
    name = db.Column(db.String(50),
                    nullable=False)
    species = db.Column(db.String(100),
                    nullable=False)
    
    img = db.Column(db.Text,
                    nullable=False,
                    default='https://image.shutterstock.com/image-vector/silhouette-pets-600w-217393339.jpg')
                    
    age = db.Column(db.String(6),
                    nullable=False)

    notes = db.Column(db.Text,
                        nullable=False,
                        default='')
    
    available = db.Column(db.Boolean,
                    default=True)




    