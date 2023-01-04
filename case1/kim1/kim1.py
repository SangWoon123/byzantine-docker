import requests
from flask import Flask
app = Flask(__name__)


@app.route('/msg')
def msg():
    msg = "sangwoon"
    return msg


@app.route('/kim1/case1')
def kim1():
    kim2_msg = requests.get('http://kim2_case1:5001/kim2')
    kim3_msg = requests.get('http://kim3_case1:5002/kim3')

# 합의값을 list에 저장,kim2가 비잔틴노드
    kim2 = list()
    kim2.append(kim2_msg.text)
    kim3 = list()
    kim3.append(kim3_msg.text)

    kim3.append(kim2[0])

    n = 3
    f = 0

    # kim3가 노드 비교
    if kim3[0] != kim3[1]:
        f += 1

    if n >= 3*f+1:
        return "kim1의 합의 메시지: [sangwoon]"+"<br>"+"kim2 합의 값: "+str(kim3[1])+"<br>"+"kim2 합의 값: "+str(kim3[0])+"<br>"+"possible"
    else:
        return "kim1의 합의 메시지: [sangwoon]"+"<br>"+"kim2 합의 값: "+str(kim3[1])+"<br>"+"kim2 합의 값: "+str(kim3[0])+"<br>"+"impossible"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
