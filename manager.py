from app import create_app
# Flask 应用工厂函数
# DEV: 开发环境   'development'
# PROD: 生产环境  'production'
# TST: 测试环境   'testing'

# 环境切换：手动指定开发环境或从环境变量读取环境
import os
config_name = os.getenv('FLASK_ENV', 'development')  # 默认使用 "development" 配置
# 默认为开发环境，按需求修改
app = create_app(config_name)

if __name__ == '__main__':
    app.run()
 
