from app.extensions import db

# 管理员表
class Admin(db.Model):
    __tablename__ = "admin"
    id = db.Column(db.Integer, primary_key=True)  # 主键
    username = db.Column(db.String(32), nullable=False, unique=True)  # 账号
    password = db.Column(db.String(64), nullable=False)  # 密码

    def __repr__(self) -> str:
        return f'<Admin {self.username}>'
