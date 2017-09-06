import os
import json

from flask import Flask, jsonify


app = Flask(__name__)

@app.route("/")
def env():
    ignore = ["FLASK_APP", "HOME", "HOSTNAME", "PATH", "TERM", "no_proxy"]

    return jsonify(env=dict({k: v for k, v in dict(os.environ).iteritems() if not k in ignore}))
