# 模板创建

## 项目结构

```markdown
├── app
│   ├── api
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   └── user.py
│   ├── models          
│   │   ├── __init__.py
│   │   └── user.py
│   ├── services.py
│   │   └── __init__.py
│   ├── static
│   ├── __init__.py
│   ├── config.py
│   └── extension.py
├── manage.py
└── README.md
```

[参考资料](https://juejin.cn/post/7148420401977098248)

## 安装的库文件

```bat
pip install Flask Flask-Cors Flask-Login PyMySQL SQLAlchemy Flask-Migrate
```

## 数据库配置

windows powershell
```shell
$env:FLASK_APP=manager.py
$env:FLASK_ENV=[development|production] # 开发环境或生产环境
```
linux
```shell
export FLASK_APP=manager.py
export FLASK_ENV=[development|production] # 开发环境或生产环境
```
## 数据库迁移

```shell
flask db init
flask db migrate
flask db upgrate
```



