import random
import string
from flask import *
import json
import time
print("Working ....")
app = Flask(__name__)


@app.route("/", methods=["GET"])
def get_user():

    vitals = {
        "id": ''.join(random.choices(string.ascii_letters +
                                     string.digits, k=25)),

        "Step Count Delta": {
            "avg": 11.426854678902204,
            "max": 1540.0,
            "min": 0.0,
            "status": "Off Track"
        },
        "Weight": {
            "avg": 72.54642240462765,
            "max": 74.55999755859375,
            "min": 71.5199966430664,
            "status": "On Track"
        }}
    user = {
        "id": ''.join(random.choices(string.ascii_letters +
                                     string.digits, k=25)),
        "name": "Sabir"
    }
    data = "name"
    return json.dumps(vitals)
