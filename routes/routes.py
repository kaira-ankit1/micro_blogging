from flask import Flask
from db.connection import Connection

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
	
	

print(Connection.getConnection())
