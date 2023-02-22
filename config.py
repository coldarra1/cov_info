HOST = '127.0.0.1'
PORT = '3306'
DATABASE = 'flask1'
USERNAME = 'root'
PASSWORD = 'admin'

DSN = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".\
    format(username=USERNAME, password=PASSWORD, host=HOST, port=PORT, db=DATABASE)

SQLALCHEMY_DATABASE_URI = DSN
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True
