from flask import Flask, request
import requests
app = Flask(__name__)

@app.route('/')
def hello_world():
    args = request.args
    username = args.get('username')
    if username is None:
        username = "testimon"
    password = args.get('password')
    if password is None:
        password = "testimon"
    regData = dict()
    regData['username'] = username
    regData['password'] = password
    r = requests.post('http://127.0.0.1/register', data=regData)
    data = {"name": "pwned", "data": r.text}
    return data