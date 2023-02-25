from flask import Flask, jsonify
from pymongo import MongoClient
from bson.objectid import ObjectId
from bson.json_util import dumps
from flask_cors import CORS, cross_origin
import pymongo


# FIXES SSL CERTIFICATE FAIL ISSUE
import certifi
ca = certifi.where()



app = Flask(__name__)
CORS(app)

client = MongoClient("mongodb+srv://tahi:74391200@cluster0.ipj2m8y.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)
db = client.remoterabbits
posts = db.posts



@app.route("/")
def read_items():
    try:
        items = list(posts.find({}))
        if not items:
            return jsonify({"error": "No data found"}), 404
            
        sorted_items = sorted(items, key=lambda item: (1 if any(value in ["Others", "All Others", "Other"] for value in item.values()) else 0, 0 if "s_link" in item else 1))
        return dumps(sorted_items) #this converts object id to yk bestie string
    except Exception as e:
        return "Error Occured: {}".format(e), 500



if __name__=='__main__':
    app.run(host='0.0.0.0', port=5000)






