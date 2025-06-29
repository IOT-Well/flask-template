import os
from .keys import DB_USERNAME, DB_PWD, DB_HOST, DB_PORT, DB_NAME

# 统一数据库连接字符串格式
def make_db_uri(db_name):
    return f'mysql+pymysql://{DB_USERNAME}:{DB_PWD}@{DB_HOST}:{DB_PORT}/{db_name}'


# 基础配置
class Config:
    SECRET_KEY = os.environ.get('KEY', DB_PWD)

    # 数据库规则
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True


# 开发环境
class DevelopmentConfig(Config):
    SQLALCHEMY_DATABASE_URI = make_db_uri(f'dev_{DB_NAME}')

    DEBUG = True


# 测试环境
class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = make_db_uri(f'test_{DB_NAME}')

    TESTING = True
    DEBUG = True


# 生产环境
class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = make_db_uri(DB_NAME)


# config dict
# 生成一个字典，用来根据字符串找到对应的配置类
config_map = {
    "development": DevelopmentConfig,
    "testing": TestingConfig,
    "production": ProductionConfig,
    "default": DevelopmentConfig
}
