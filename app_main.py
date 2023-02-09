import datetime

from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='./static/')

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/word", methods=["GET"])
def word_get():
    word_list = list(db.register.find({},{'_id':False}).sort("_id",-1))
    return jsonify({'words': word_list})



@app.route("/word_detail", methods=["GET"])
def word_detail():
    return render_template('word_detail.html')

@app.route("/word_detail_info", methods=["GET"])
def word_get_detail():
    word_detail = request.args.get("keyword")
    print(word_detail)
    # word_list = db.register.find_one({}, {'_id': False})
    word_list = list(db.register.find({'word': word_detail}, {'_id': False}))
    print(word_list)
    return jsonify({'words': word_list})

@app.route("/counting", methods=["GET"])
def count_get():
    db_count = db.register.count_documents({})
    return jsonify({'counts': db_count})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)
