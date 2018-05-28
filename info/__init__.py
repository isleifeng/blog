import logging
from logging.handlers import RotatingFileHandler

import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

db = SQLAlchemy()

# 提供一个函数, 工厂方法,方便根据不同的成熟, 实现不同的配置加载
def create_app(config_name):
    # 配置项目日志
    setup_log(config_name)

    app = Flask(__name__)
    app.config.from_object(config_name)

    # 插件数据库
    db.init_app(app)

    # 创建redis对象
    redis_store = redis.Redis(host=config_name.REDIS_HOST, port=config_name.REDIS_PORT)

    # 开启CSRF保护 -> 开启csrf_token对比机制, 需要设置SECRET_KEY
    CSRFProtect(app)

    # 设置Flask-Session扩展， 将存在浏览器中的session数据， 同步到服务器指定的地址中（一般用redis储存）
    Session(app)

    return app

def setup_log(config_name):
    # 设置日志的记录等级
    logging.basicConfig(level=config_name.LOG_LEVEL)  # 调试debug级
    # 创建日志记录器，指明日志保存的路径、每个日志文件的最大大小、保存的日志文件个数上限
    file_log_handler = RotatingFileHandler("logs/log", maxBytes=1024 * 1024 * 100, backupCount=10)
    # 创建日志记录的格式 日志等级 输入日志信息的文件名 行数 日志信息
    formatter = logging.Formatter('%(levelname)s %(filename)s:%(lineno)d %(message)s')
    # 为刚创建的日志记录器设置日志记录格式
    file_log_handler.setFormatter(formatter)
    # 为全局的日志工具对象（flask app使用的）添加日志记录器
    logging.getLogger().addHandler(file_log_handler)
