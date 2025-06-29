from .admin import admin_blueprint
from .user import user_blueprint

DEFAULT_BLUEPRINT = [
    (admin_blueprint, '/api/admin/'),
    (user_blueprint, '/api/user/')
]


def config_blueprint(app):
    for blueprint, prefix in DEFAULT_BLUEPRINT:
        app.register_blueprint(blueprint, url_prefix=prefix)
