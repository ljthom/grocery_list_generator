from sqlalchemy.sql import func
from pantry import db


class BaseModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    entry_date = db.Column(db.DateTime(timezone=True), server_default=func.now())
    entry_update = db.Column(db.DateTime(timezone=True), onupdate=func.now())
