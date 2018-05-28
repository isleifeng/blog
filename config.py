import redis


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

    DEBUG = True