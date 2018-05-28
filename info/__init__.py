import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session
from config import Config

app = Flask(__name__)
app.config.from_object(Config)


# 插件数据库
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护 -> 开启csrf_token对比机制, 需要设置SECRET_KEY
CSRFProtect(app)

# 设置Flask-Session扩展， 将存在浏览器中的session数据， 同步到服务器指定的地址中（一般用redis储存）
Session(app)