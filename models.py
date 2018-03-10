"""SQLAlchemy models for MyAstroBase."""

from app import db

class Eyepiece(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    focal_length = db.Column(db.Float)
    fov = db.Column(db.Float)
