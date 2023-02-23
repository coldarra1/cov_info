import config as config
from flask import Flask
from gevent import pywsgi

from exts import db

app = Flask(__name__)
# 加载配置文件
app.config.from_object(config)
# db绑定app
db.init_app(app)


@app.route('/', methods=["GET", "POST"])
def index():
    return "hello!"


if __name__ == '__main__':
    server = pywsgi.WSGIServer(('127.0.0.1', 5000), app)
    server.serve_forever()
