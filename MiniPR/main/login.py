from main import * #from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다 

blueprint = Blueprint("login" , __name__ , url_prefix="/login")

@blueprint.route("/") #<- 데코레이터
def login_template():
    return render_template("login.html")