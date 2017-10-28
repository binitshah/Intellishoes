from flask import Flask
from flask import jsonify
import pymongo

app = Flask(__name__)
uri = 'mongodb://heroku_qg4xxhbq:2jb487u6ota241oqoh7vgpd9tj@ds119210.mlab.com:19210/heroku_qg4xxhbq'
client = pymongo.MongoClient(uri)
db = client.get_default_database()

@app.route('/')
def index():
    return "Hi! Welcome to Intellishoes!"

@app.route('/post_ip_address/<ip_address')
def post_ip_address(ip_address):
    return ip_address

if __name__ == "__main__":
    app.run()