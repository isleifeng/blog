from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from info import app, db

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
