"""
rmon配置文件
"""
import os

class DevConfig:
    """
    开发环境配置
    """

    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #数据库在内存中，flask app退出后数据会丢失
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    TEMPLATES_AUTO_RELOAD = True

class ProductConfig(DevConfig):
    """
    生产环境配置
    """
    DEBUG = False

    #sqlite数据库文件路径
    path = os.path.join(os.getcwd(),'rmon.db').replace('\\','/')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///%s' % path


