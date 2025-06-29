from flask import Blueprint, request, jsonify
from app.utils.md5 import *
from app.models.user import User
from app.extensions import db
user_blueprint = Blueprint('user', __name__)


@user_blueprint.route('/register', methods=['POST'])
def user_register():
    try:
        req_data = request.form
        username = req_data.get("username")
        password = req_data.get("password")
        password = spw(password)
        nickname = "用户" + username
        user = User(username=username, password=password, nickname=nickname)
    except Exception as e:
        print(e)
        return jsonify(code=400, msg="注册失败, 检查请求格式")

    try:
        db.session.add(user)
        db.session.commit()
        return jsonify(code=200, msg="注册成功", username=username, user_id=user.id)
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify(code=400, msg="注册失败")
