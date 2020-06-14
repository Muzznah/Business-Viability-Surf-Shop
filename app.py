from flask import Flask
#Create flast instance.
app = Flask(__name__)
#Define the starting point.
@app.route('/')
def hello_world():
	return 'Hello world'
