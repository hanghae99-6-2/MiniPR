from main import * #from main import * : main에 선언된 모든 값을 가져온다 , __init__ file에 선언된 라이브러리를 가져와 사용할 수 있음.
from flask import Blueprint
import datetime

#객체 = Blueprint("name" , __name__ , url_prefix="") : (이름, 모듈명, URL 프리픽스 값)
#이름은 url_for함수에서 사용되며 , 모듈명은 init.py에서 선언한 모듈을 뜻함 , url_prefix="주소"의 주소에는 브라우져에서 선언될 url을 입력한다 

blueprint = Blueprint("community" , __name__ , url_prefix="/community")

@blueprint.route("/") #<- 데코레이터
def write_template():
    #데이터들을 렌더 템플릿과 함께 리턴해줘야한다.
    community_db = list(db.community.find({},{'_id':False}))
    community = community_db[0]['community']
    
    comment_db = list(db.comment.find({},{'_id':False}))
    comment = comment_db[0]['comment']

    return render_template("community.html" , community = community , comment = comment)

def db_post():
    user_index = 1 #로그인에서 넘겨준 유저의 인덱스 번호를 넘겨줄 것
    email = "plo@naver.com" #로그인에서 넘겨준 유저의 이메일을 넘겨줄 것
    day = datetime.datetime.now() 
    now = day.strftime('%Y-%m-%d')
    comment = "완성할 수 있다 화이팅" #클라이언트에서 받은 유저의 input을 받아올 것

    doc_community = {'comment': {
        "user_name" : user_index ,
        "email" : email , 
        "now" : now ,
        "comment" : comment
        }}
    db.comment.insert_one(doc_community)
    
    desc1 = "파워트레인/성능 E-Turbo 1.35 직분사 가솔린 엔진, VT40 무단 변속기, Stop & Start 시스템(ON/OFF 버튼 포함), 액티브 에어로 셔터, 속도 감응형 전자식 파워 스티어링(R-EPS)"
    desc2 = "외관 사양 알로이 휠, 프로젝션 헤드램프, 어쿠스틱 윈드실드 글래스(차음/자외선 차단), 자외선 차단 유리(전체), 크리스탈 LED 주간주행등, LED 보조제동등, LED 테일 램프, LED 방향지시등 일체형 아웃사이드 미러(전동조절/열선내장/전동접이식), 크롬 도어핸들"
    name = "hyuk" #메인의 db에 저장된 데이터를 가져올 것
        
    #key안에 li 안에 key안에 val
    doc = {'community': {
        "desc1" : desc1 ,
        "desc2" : desc2 ,
        "name" : name ,
        }}
    db.community.insert_one(doc)


db_post()
