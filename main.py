from flask import *
import json, time
print("Working ....")
app=Flask(__name__)
@app.route("/",methods=["GET"])
def get_user():
    user={
        "id":time.time()
    }
    return json.dumps(user)

