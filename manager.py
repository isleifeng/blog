from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route('/index')
def index():
    return 'hello flask'


if __name__ == '__main__':
    app.run(debug=True)
