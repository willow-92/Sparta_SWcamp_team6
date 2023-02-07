from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='./static/')

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
   return render_template('')


@app.route("/word", methods=["GET"])
def word_get():
    word_list = list(db.register.find({'name':'날슝이'},{'_id':False}))
    count = db.register.count_documents({})
    print(count)
    return jsonify({'word':word_list})



if __name__ == '__main__':
   app.run('0.0.0.0', port=9999, debug=True)