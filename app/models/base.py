from app.extensions import db
from datetime import datetime


class BaseModel:
    creat_time = db.Column(db.DateTime, default=datetime.now())
    update_time = db.Column(
        db.DateTime, default=datetime.now(), onupdate=datetime.now())
