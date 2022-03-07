from main import app
# run.py에서는 main폴더에서 __init__에 선언된 app객체를 가져와 실행 및

# host(모든 public ip의 접근 가능) 및 port번호 , debug=True(어플리케이션 실행시 파라미터로 넘겨주겠다)를 선언한다. (마지막 코드라인)

if __name__ == '__main__':  # 우리가 실행하는 서버(port = 5000)이 유일한 서버입니다.
    app.run(host='0.0.0.0', port=5001, debug=True)
