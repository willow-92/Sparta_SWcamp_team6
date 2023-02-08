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
    word_list = list(db.register.find({},{'_id':False}).sort("_id",-1) )
    return jsonify({'words':word_list})


@app.route("/word", methods=["GET"])
def time_get():
    time_list = list(db.register.find({'created_at'}))
    return jsonify({'times':time_list})


@app.route("/counting", methods=["GET"])
def count_get():
    db_count = db.register.count_documents({})
    return jsonify({'counts': db_count})


if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)