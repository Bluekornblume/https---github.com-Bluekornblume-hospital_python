from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return "欢迎来到病院管理システム！"