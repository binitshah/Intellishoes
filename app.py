from os.path import join, dirname, os
from dotenv import load_dotenv
from flask import Flask
from flask import jsonify
import pymongo

app = Flask(__name__)
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
uri = os.environ.get("MONGODB_URI")
client = pymongo.MongoClient(uri)
db = client.get_default_database()

@app.route('/')
def index():
    return "Hi! Welcome to Intellishoes!"

@app.route('/post_ip_address/<ip_address>')
def post_ip_address(ip_address):
    return ip_address

if __name__ == "__main__":
    app.run()