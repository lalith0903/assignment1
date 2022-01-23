pip install flask requests

from flask import Flask, jsonify, make_response
import requests
import os
import simplejson as json

with open("{}/database/users.json".format(database_path), "r") as f:
    usr = json.load(f)
	
@app.route("/", methods=['GET'])
def hello():
    ''' Greet the user '''

    return "Hey! The service is up, how about doing something useful"

if __name__ == '__main__':
    app.run(port=5000, debug=True)