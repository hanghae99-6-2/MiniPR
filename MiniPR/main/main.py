from main import render_template, jsonify, request
from flask import Blueprint

from pymongo import MongoClient
client = MongoClient('DB주소')                                                                             #DB 주소 입력
db = client.dbsparta

blueprint = Blueprint("main" , __name__ , url_prefix="/")

@blueprint.route("/") #<- 데코레이터
def main_template():
    return render_template("main.html")

# 메인 페이지 재료 클릭 시 재료별 이미지출력
#@blueprint.route("/cars/type", methods=["GET"])                                                                  #mongoDB의 /cars 에서 GET 방식으로 불러옴
# db에서 키워드로 db리스트 가져오기
#def car_get():                                                                                             #car_get이라는 함수 설정
#   list = request.args.get('type')                                                                        #key값이 type인걸 알고 있을 때, value를 바로 조회
#   car_list = list(db.cars.find({'type': {'$regex': keyword}}))                                           #mongoDB의 cars에서 type이 $regex -> 포함된 문자열을 리스트 가져오기
#   return jsonify({'cars': car_list}