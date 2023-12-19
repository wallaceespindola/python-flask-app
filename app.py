from flask import Flask
import datetime;

app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Server is UP!!! <br><br>Python Flask Web App is running! <br><br>Current date-time: ' + str(datetime.datetime.now())
    
