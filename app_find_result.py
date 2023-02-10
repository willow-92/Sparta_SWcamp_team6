# flask 서버 구동
from flask import Flask, render_template, request, jsonify
from bson.objectid import ObjectId

app = Flask(__name__)

# mongo db
from pymongo import MongoClient
client = MongoClient('mongodb+srv://sw-camp-team6:team6@cluster0.3hlvzux.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def search_result():
    return render_template('search_result.html')


@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    results = list(db.register.find({"word": {"$regex": str(query), "$options": "i"}}, {'_id': False}))
    return jsonify({'key': results})


if __name__ == "__main__":
    app.run(debug=True)
