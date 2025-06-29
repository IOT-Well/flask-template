from flask import Flask
from flask_cors import CORS
from app.api import config_blueprint
from app.extensions import config_extensions
from app.config import config_map

def create_app(config_name):
   
    # 实例化 app
    app = Flask(__name__)

    # 加载配置项
    app.config.from_object(config_map.get(config_name))
    
    # 加载拓展
    config_extensions(app)
    
    # 加载蓝图
    config_blueprint(app)

    # 全局跨域
    CORS(app, supports_credentials=True)

    return app