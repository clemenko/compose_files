from flask import Flask, render_template
from redis import Redis
from flaskext.mysql import MySQL

import os

app = Flask(__name__)
redis = Redis(host='redis', port=6379)
server_name = os.getenv('SRV_NAME')
server_health_key = '{0}_health'.format(server_name)

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'EmpData'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route('/health/on')
def health_on():
    redis.set(server_health_key, 'on')
    return 'Health key {0} set to on!'.format(server_health_key)

@app.route('/health/off')
def health_off():
    redis.set(server_health_key, 'off')
    return 'Health key {0} set to off!'.format(server_health_key)

@app.route('/health/check')
def health_check():
    health = redis.get(server_health_key)
    if health == 'on':
        return 'healthy', 200
    else:
        return 'not healthy', 500

@app.route('/healthy')
def healthy():
    return 'healthy', 200

@app.route('/version')
def version():
    return '2.0', 200

@app.route('/')
def index(server_name=None):
    redis.incr('hits')
    server_name = os.getenv('HOSTNAME')
    return render_template('index.html', hits=redis.get('hits'), server_name=server_name)

if __name__ == '__main__':
    health_on()
    app.run(host='0.0.0.0')
