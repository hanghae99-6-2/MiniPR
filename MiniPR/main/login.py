from main import *  # from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint
import jwt
from datetime import datetime, timedelta
import hashlib


# 객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
# 이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다

blueprint = Blueprint("login", __name__, url_prefix="/login")

SECRET_KEY = 'CAR'



@blueprint.route("/")  # <- 데코레이터
def login_template():
    return render_template("login.html")

@blueprint.route('/sign_in', methods=['POST'])
def sign_in():

    # 로그인
    username_receive = request.form['username_give']
    password_receive = request.form['password_give']

    pw_hash = hashlib.sha256(password_receive.encode('utf-8')).hexdigest()  # 비밀번호 암호화를 위한 해쉬값을 만들어 줌.
    result = db.users.find_one({'username': username_receive,
                                'password': pw_hash})  # 아이디와 패스워드가 매칭되는지 판단을 해줌. 매칭되는 사람이 있다면! 로그인에 성공 한것. 매칭이 안되면 회원가입을 해야함.

    if result is not None:  # result가 있다면!
        payload = {
            'id': username_receive,
            'exp': datetime.utcnow() + timedelta(seconds=60 * 60 * 24)  # 로그인 24시간 유지
        }
        token = jwt.encode(payload, SECRET_KEY, algorithm='HS256') # jwt 토큰을 발행. 놀이공원 자유입장권과 같은 것. 어떤 사람이 언제까지 입장이 유효하다를 적시해줌.
        # 토큰이 제대로 발행되었는지 확인하려면, 오른쪽 마우스 검사 누르고, 개발자 콘솔을 열면 Application탭을 눌러서 cookies가 나와 있음.
        return jsonify({'result': 'success', 'token': token})
        # 찾지 못하면,
    else:
        return jsonify({'result': 'fail', 'msg': '아이디/비밀번호가 일치하지 않습니다.'})

