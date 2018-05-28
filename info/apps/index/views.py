from . import index
from info import redis_store


@index.route('/')
def index():
    redis_store.set('n', 'a')
    return 'index'
