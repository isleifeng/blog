from flask import Flask
from flask_script import Manager
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    # 配置SQLALchemy
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1/infomation'
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # 是否追踪改变


app = Flask(__name__)
app.config.from_object(Config)
manager = Manager(app)

db = SQLAlchemy(app)


@app.route('/')
def index():
    return 'hello flask'


if __name__ == '__main__':
    app.run()
