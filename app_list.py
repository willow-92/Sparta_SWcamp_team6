import datetime

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='./static/')

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('list.html')

@app.route("/read", methods=["GET"])
def list_get():
    word_list = list(db.register.find({},{'_id':False}).sort("_id",-1))
    return jsonify({'words': word_list})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)