import requests
from flask import Flask
app = Flask(__name__)


@app.route('/msg')
def msg():
    msg = "sangwoon"
    return msg


@app.route('/kim1/case2')
def kim1():
    kim2_msg = requests.get('http://kim2_case2:5051/kim2')
    kim3_msg = requests.get('http://kim3_case2:5052/kim3')
    kim4_msg = requests.get('http://kim4_case2:5053/kim4')

# 합의값을 list에 저장,kim3가 비잔틴노드
    kim2 = list()
    kim2.append(kim2_msg.text)

    kim3 = list()
    kim3.append(kim3_msg.text)

    kim4 = list()
    kim4.append(kim4_msg.text)

    kim2.append(kim3[0])  # 다른 노드의 합의값 저장
    kim2.append(kim4[0])

    kim4.append(kim2[0])  # 다른 노드의 합의값 저장
    kim4.append(kim3[0])

    kim2_count = {}
    kim4_count = {}

    kim2_choice = False
    kim4_choice = False

    for i in kim2:
        try:
            kim2_count[i] += 1
        except:
            kim2_count[i] = 1

    choice = kim2_count.values()
    choice = max(choice)

    if choice != 1:
        kim2_choice = True

    for i in kim4:
        try:
            kim4_count[i] += 1
        except:
            kim4_count[i] = 1

    choice = kim4_count.values()
    choice = max(choice)

    if choice != 1:
        kim4_choice = True

    if kim2_choice and kim4_choice:
        return "kim1의 합의 메시지: [sangwoon]"+"<br>"+"kim2 합의 값: "+str(kim2[0])+"<br>"+"kim3 합의 값: "+str(kim3[0])+"<br>"+"kim4 합의 값: "+str(kim4[0])+"<br>"+"possible"
    else:
        return "kim1의 합의 메시지: [sangwoon]"+"<br>"+"kim2 합의 값: "+str(kim2[0])+"<br>"+"kim3 합의 값: "+str(kim3[0])+"<br>"+"kim4 합의 값: "+str(kim4[0])+"<br>"+"impossible"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5050, debug=True)
