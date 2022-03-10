from re import I
from main import * #from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint
import datetime

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다 

blueprint = Blueprint("community" , __name__ , url_prefix="/community")

@blueprint.route("/") #<- 데코레이터
def community_template():
    user = list(db.users.find({},{'_id':False}))
    cars = list(db.cars.find({},{'_id':False}))

    return render_template("community.html" , car = cars)
        
@blueprint.route("/comment_post" , methods = ["GET" "POST"])
def comment_post():
        SECRET_KEY = 'CAR'
        token_receive = request.cookies.get('token') #쿠키에서 토큰을 받아올 것
        payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256']) #로그인한 페이지이기 때문에 jwt에 token정보를 읽어옴
        
        user_info = db.users.find_one({"username": payload["id"]}) #페이로드와 동일한 데이터
         
        index_receive = request.form['index_give']
        comment_receive = request.form['comment_give']#클라이언트에서 받은 유저의 input을 받아올 것
        day = datetime.datetime.now()  #데이터가 들어가는 실시간 시간 저장
        now = day.strftime('%Y-%m-%d')
        
        
        comment = comment_receive #유저의 input 값
        
        doc = {'comment': {
            "user_name" : user_info['username'] , 
            "user_email" : user_info['email'],
            "now" : now ,
            "comment" : comment
            }}
        
        db.cars.insert_one(doc)
        return ({"msg" : "댓글 저장 완료!"})


@blueprint.route("/post_card" , methods = ["POST"])
def post_card():
    data = list(db.cars.find({},{'_id':False}))
    
    return jsonify({'card': data})
    
 

 #     #1. GET : DB에서 Data를 찾아 Client에서 호출할 수 있게 return값을 할당
 # 2. POST : Client에서 Data를 받아 DB에 저장
 # - Client
 #     1. GET : Server에서 Data를 받아 posting
 #     2. POST : 사용자의 Input값을 data형식 지정 후 Server에 전송



# db_post()
# 
# ## 로그인 기능구현 관련
# @app.route('/sign_in', methods=['POST'])
# def sign_in():
#     # 로그인
#     username_receive = request.form['username_give']
#     password_receive = request.form['password_give']

#     pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()
#     result = db.users.find_one({'username': username_receive, 'password': pw_hash})

#     if result is not None:
#         payload = {
#          'id': username_receive,
#          'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
#         }
#         token = jwt.encode(payload, SECRET_KEY, algorithm='HS256').decode('utf-8')

#         return jsonify({'result': 'success', 'token': token})
#     # 찾지 못하면
#     else:
#         return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})