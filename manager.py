import redis
from flask import Flask, session
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_session import Session

class Config(object):

    # 配置SQLALchemy
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/infomation'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪改变

    # 配置redis
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379

    # import os, base64
    # base64.b64encode(os.urandom(32))
    # b'PixrUteifKbnrb676vFfva1XqhFLvwP+O93XanzkORo='
    SECRET_KEY = 'PixrUteifKbnrb676vFfva1XqhFLvwP+O93XanzkORo='

    # 配置flask-session扩展
    SESSION_TYPE = 'redis'  # 设置要同步的位置
    SESSION_REDIS = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    SESSION_USE_SIGNER = True  # 开启签名,保证数据安全
    SESSION_PERMANENT = 3600 * 24 * 7  # 设置session过期时间



app = Flask(__name__)
app.config.from_object(Config)
app.debug = True
manager = Manager(app)

# 插件数据库
db = SQLAlchemy(app)

# 创建redis对象
redis_store = redis.Redis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护 -> 开启csrf_token对比机制, 需要设置SECRET_KEY
CSRFProtect(app)

# 设置Flask-Session扩展， 将存在浏览器中的session数据， 同步到服务器指定的地址中（一般用redis储存）
Session(app)

@app.route('/')
def index():
    session['name'] = 'zhangsan'
    return 'hello flask'


if __name__ == '__main__':
    manager.run()
