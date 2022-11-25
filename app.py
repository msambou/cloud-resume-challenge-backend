	
from collections import namedtuple
from random import choice
 
from flask import Flask, jsonify
import serverless_wsgi
from Database import Database
import json

# Instantiate Database
database = Database()

cors_headers = {
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET,PUT'
}
 
app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_greetings():
    return "Hello and Welcome to Mike's Cloud Resume Challenge. -1"

@app.route("/view-count", methods=["GET"])
def get_view_count():
    response = database.get_count()
    return jsonify(response)

@app.route("/view-count", methods=["PUT"])
def update_view_count():
    response = database.increment_count()
    return jsonify(response)

def handler(event, context):
    return serverless_wsgi.handle_request(app, event, context)