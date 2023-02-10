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


# 야매로 검색 데이터를 DB에 전달
@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("query")
    results = list(db.register.find({"word": {"$regex": str(query), "$options": "i"}}, {'_id': False}))
    return jsonify({'key': results})





# # 2월 9일 chat gpt가 짜준 코드 (아직 잘 작동)
# @app.route("/search", methods=["POST"])
# def search():
#     query = request.form.get("query")
#     print("불러온 query의 값 : ",query)
#     results = db.register.find({"word": {"$regex": str(query), "$options": "i"}}, {'_id': False})
#     return jsonify([result for result in results])




# 2월 9일 새벽에 짜놨다가 에러가 났던 코드
# @app.route("/find", methods=["POST", "GET"])
# def receive_keyword():
#     keyword = request.form['keyword_give']
#     print("db 조회 전 받아온 값 : ", keyword)
#     result = list(db.register.find({'word': keyword}, {'_id': False}))
#     return jsonify({'result': result})

if __name__ == "__main__":
    app.run(debug=True)

    # register = db.register
    # print(keyword)
    # # search for documents containing the keyword in "word" and "desc" fields
    # results = register.find({'word': keyword})
    # return jsonify({"result": "success", "data": results})
    # print(results)

    # # convert each ObjectId to a string
    # results = [{"_id": str(results["_id"]), "word": results["word"]}]
    # print(results)
    # #
    # return jsonify({"result": "success", "data": results})




#     keyword = request.form.get["keyword"]
#     print(keyword)
#
#     # 몽고 db 내에서 조회하기
#     results = db.register.find({"$or": [{"word": keyword}]})
#
#     # ObjectID를 String으로 변환
#     results = results = [{"_id": str(result["_id"]), "word": result["word"]} for result in results]
#
#     print(results)
#     # return jsonify({"result": "success", "data":results})
#
# # @app.route("/find", methods=["GET"])
# # def get_keyword():
# #     keyword_list = db.register.find_one(receive_keyword())
# #     print(keyword_list)






    #
    # db.register.find_one(found_result)
    #
    # if result:
    #     return jsonify({"word": result["word"], "description": result["description"]})
    # else:
    #     return render_template('search_result_none.html')