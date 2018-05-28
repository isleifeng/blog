from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import create_app, db
from config import DevlopmentConfig

# 通过create_app, 传递不同的配置信息， 实现manager以不同模式来启动
app = create_app(DevlopmentConfig)
# 创建 manager
manager = Manager(app)

# 创建迁移对象
Migrate(app, db)

# 给manager绑定迁移命令
manager.add_command('db', MigrateCommand)


@app.route('/')
def index():
    # session['name'] = 'zhangsan'
    return 'hello flask'


if __name__ == '__main__':
    manager.run()
