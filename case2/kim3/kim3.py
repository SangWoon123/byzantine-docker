import requests
from flask import Flask
app = Flask(__name__)


@app.route('/kim3')
def kim3():
    return_msg = requests.get("http://kim1_case2:5050/msg")
    return_msg = return_msg.text[::-1]
    return return_msg


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5052, debug=True)
