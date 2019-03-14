import os
from flask import Flask

from rmon.views import api
from rmon.models import db
from rmon.config import DevConfig, ProductConfig

def create_app():
    app = Flask('rmon')
    env = os.environ.get('RMON_ENV')
    if env in ('pro','prod','product'):
        app.config.from_object(ProductConfig)
    else:
        app.config.from_object(DevConfig)

    app.config.from_envvar('RMON_SETTINGS',silent=True)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #注册Blueprint
    app.register_blueprint(api)

    #初始化数据库
    db.init_app(app)

    #如果是开发环境则创建所有数据库表
    if app.debug:
        with app.app_context():
            db.create_all()
    return app
