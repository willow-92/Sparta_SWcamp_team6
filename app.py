# flask 서버 구동
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.hy28zsk.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
    return render_template('index.html')

@app.route("/detail", methods=["POST"])
def reply_post():
    name_receive = request.form['name_give']
    comment_receive = request.form['comment_give']
    posttime_receive = request.form['posttime_give']

    doc = {
        'name': name_receive,
        'comment': comment_receive,
        'posttime': posttime_receive,
    }
    db.replys.insert_one(doc)

    return jsonify({'msg': '작성 완료!'})

@app.route("/detail", methods=["GET"])
def reply_get():
    reply_list = list(db.replys.find({}, {'_id': False}))
    return jsonify({'replys': reply_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)