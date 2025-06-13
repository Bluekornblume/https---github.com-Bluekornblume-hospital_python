from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config.Config)

    db.init_app(app)

    # 导入并注册路由蓝图
    from app.routes import bp as main_bp
    app.register_blueprint(main_bp, url_prefix='/api')

    return app