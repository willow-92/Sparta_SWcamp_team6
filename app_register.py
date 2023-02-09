# flask 서버 구동
from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def main():
    return render_template('word_register.html')


@app.route("/word_register", methods=["POST"])
def word_register_post():
    newword_receive = request.form['newword_give']
    nickname_receive = request.form['nickname_give']
    img_url_receive = request.form['img_url_give']
    youtube_url_receive = request.form['youtube_url_give']
    desc_receive = request.form['desc_give']
    age_tag_receive = request.form['age_tag_give']
    # 이게 뭘까요? created_at_receive = request.form['created_at_give']


    doc = {
        'newword': newword_receive,
        'nickname': nickname_receive,
        'img_url': img_url_receive,
        'youtube_url': youtube_url_receive,
        'desc_url': desc_receive,
        'age_tag': age_tag_receive
        # 'created_at': created_at_receive,

    }

    db.register.insert_one(doc)
    return jsonify({'msg': '작성 완료!'})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)