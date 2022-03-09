#main에 선언된 모든 값을 가져온다
from main import *
from flask import Blueprint

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다

blueprint = Blueprint("main" , __name__ , url_prefix="/")

@blueprint.route("/")                                                                                     #route:url을 함수와 연결하는데 사용
def main_template():                                                                                      #└ "/~"는 main_template함수와 연결되어 http://localhost:5000/~ 를 방문하면 return값이 불러와짐
    return render_template("main.html")                                                                   #main.html 불러옴, return:결과값을 돌려주는 명령어

# 메인 페이지 재료 클릭 시 재료별 이미지출력
# @blueprint.route("/car", methods=["GET"])                                                                     #mongoDB의 / 에서 GET 방식으로 불러옴

# db에서 키워드로 db리스트 가져오기
def car_get():                                                                                             #car_get이라는 함수 설정
    list = request.args.get('type')                                                                        #key값이 type인걸 알고 있을 때, value를 바로 조회
    # car_list = list(db.cars.find({'type': {'$regex': keyword}}))                                           #mongoDB의 cars에서 type이 $regex -> 포함된 문자열을 리스트 가져오기
    # return jsonify({'cars': car_list})