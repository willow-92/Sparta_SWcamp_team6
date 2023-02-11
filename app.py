# flask 서버 구동
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/list')
def lists():
    return render_template('list.html')

@app.route('/detail')
def detail():
    return render_template('word_detail.html')
@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/register')
def register():
    return render_template('word_register.html')

@app.route("/word", methods=["GET"])
def desc_get():

    word_list = list(db.register.find({}, {'_id': False}))
    return jsonify({'replys': word_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)