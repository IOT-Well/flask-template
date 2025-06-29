from app.extensions import db
from .base import BaseModel

class User(BaseModel, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(32), nullable=False, unique=True)  # 账号
    nickname = db.Column(db.String(32), nullable=True, unique=True)  # 昵称
    password = db.Column(db.String(64), nullable=False)  # 密码

    def __init__(self, username, password, nickname):
        self.username = username
        self.password = password
        self.nickname = nickname

    def __repr__(self) -> str:
        return f'<User {self.username}>'