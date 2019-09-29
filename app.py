from flask import Flask
from redis import Redis, RedisError
from flask_restful import Resource, Api
import os
import socket 

app = Flask(__name__)
api = Api(app)

redis = Redis(host="redis-server", db=0, socket_connect_timeout=2, socket_timeout=2)

@app.route("/")
def hello():
    try:
        visits = redis.incr("counter")
    except RedisError:
        visits = "<i>cannot connect to Redis server to count</i>"
    html = "<h3>Hello World!</h3>\n" \
           "<b>Hostname:</b> {hostname}<br/>\n" \
           "<b>Visits:</b> {visits}\n"
    return html.format(hostname=socket.gethostname(), visits=visits)

#api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=80)