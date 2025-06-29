from flask import Blueprint
from app.models.admin import Admin

admin_blueprint = Blueprint('admin', __name__)


@admin_blueprint.route('/', methods=['GET'])
def index():
    return 'Hello, admin!'
