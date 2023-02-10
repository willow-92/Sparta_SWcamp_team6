from flask import Flask, render_template, request, jsonify
app = Flask(__name__, static_folder='./static/')

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/Cluster0?retryWrites=true&w=majority')
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

@app.route('/shop')
def shop():
    return render_template('shop.html')

@app.route('/register')
def register():
    return render_template('word_register.html')


@app.route("/word", methods=["GET"])
def word_get():
    word_list = list(db.register.find({},{'_id':False}).sort("_id",-1))
    return jsonify({'words': word_list})

@app.route("/word", methods=["GET"])
def time_get():
    time_list = list(db.register.find({'created_at'}))
    return jsonify({'times': time_list})


@app.route("/word_detail", methods=["GET"])
def word_detail():
    return render_template('word_detail.html')

@app.route("/word_detail_info", methods=["GET"])
def word_get_detail():
    word_detail = request.args.get("keyword")
    print(word_detail)
    #word_list = db.register.find_one({}, {'_id': False})
    word_list = list(db.register.find({'word': word_detail}, {'_id': False}))
    print(word_list)
    return jsonify({'words': word_list})


@app.route("/counting", methods=["GET"])
def count_get():
    db_count = db.register.count_documents({})
    return jsonify({'counts': db_count})

@app.route('/')
def search_result():
    return render_template('search_result.html')

@app.route("/read", methods=["GET"])
def list_get():
    word_list = list(db.register.find({},{'_id':False}).sort("_id",-1))
    return jsonify({'words': word_list})


# 야매로 검색 데이터를 DB에 전달
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    results = list(db.register.find({"word": {"$regex": str(query), "$options": "i"}}, {'_id': False}))
    return jsonify({'key': results})

#단어 등록 DB에 보내기
@app.route("/word_register", methods=["POST"])
def word_register_post():
    word_receive = request.form['word_give']
    name_receive = request.form['name_give']
    img_url_receive = request.form['img_url_give']
    youtube_url_receive = request.form['youtube_url_give']
    desc_url_receive = request.form['desc_url_give']
    age_tag_receive = request.form['age_tag_give']
    # 이게 뭘까요? created_at_receive = request.form['created_at_give']

    doc = {
        'word': word_receive,
        'name': name_receive,
        'img_url': img_url_receive,
        'youtube_url': youtube_url_receive,
        'desc_url': desc_url_receive,
        'age_tag': age_tag_receive
        # 'created_at': created_at_receive,

    }

    db.register.insert_one(doc)
    return jsonify({'msg': '작성 완료!'})

@app.route("/word", methods=["GET"])
def desc_get():
    word_list = list(db.register.find())
    print(word_list)
    return render_template('temp_word_register.html')

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)