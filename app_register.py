# flask 서버 구동
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def main():
    return render_template('temp_word_regist.html')

@app.route('/home')
def home():
    return render_template('temp_word_regist.html')

@app.route('/list')
def list():
    return render_template('temp_word_regist.html')

@app.route("/word", methods=["POST"])
def reply_post():

    word_receive = request.form['word_give']
    name_receive = request.form['name_give']
    img_url_receive = request.form['img_url_give']
    youtube_url_receive = request.form['youtube_url_give']
    desc_url_receive = request.form['desc_url_give']
    created_at_receive = request.form['created_at_give']
    age_tag_receive = request.form['age_tag_give']

    doc = {
        'word': word_receive,
        'name': name_receive,
        'img_url': img_url_receive,
        'youtube_url': youtube_url_receive,
        'desc_url': desc_url_receive,
        'created_at': created_at_receive,
        'age_tag': age_tag_receive,
    }

    # db.register.insert_one(doc)
    print(doc)
    # return jsonify({'msg': '작성 완료!'})

# @app.route("/detail", methods=["GET"])
# def reply_get():
#     reply_list = list(db.replys.find({}, {'_id': False}))
#     return jsonify({'replys': reply_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)