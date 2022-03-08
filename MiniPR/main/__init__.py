from flask import Flask , render_template , request , jsonify , session 
from pymongo import MongoClient
import certifi

#db 연결
ca = certifi.where()
client = MongoClient('mongodb+srv://notflix:1514@cluster0.jtaa3.mongodb.net/Cluster0?retryWrites=true&w=majority',tlsCAFile=ca)
db = client.notflix

#__init__.py 파일에선 app 객체를 선언하고 각종 모듈, 데이터베이스, 블루프린트 등 값을 설정한다

from . import main       #from . import main : main.py의 내용을 호출하겠다.
from . import login    
from . import sign_up   
from . import community 


app = Flask(__name__)

app.register_blueprint(main.blueprint) # (main.blueprint) main.py에서 사용할 blueprint객체를 blueprint로 설정할거야
app.register_blueprint(login.blueprint) 
app.register_blueprint(sign_up.blueprint)
app.register_blueprint(community.blueprint)

