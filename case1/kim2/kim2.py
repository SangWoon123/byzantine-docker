import requests
from flask import Flask
app = Flask(__name__)


@app.route('/kim2')
def kim2():
    return_msg = requests.get("http://kim1_case1:5000/msg")
    return_msg = return_msg.text[::-1]
    return return_msg


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
