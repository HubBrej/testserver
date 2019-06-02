from flask import request,Flask,jsonify
from flask_cors import CORS, cross_origin
app=Flask(__name__)

CORS(app)

@app.route('/auth', methods=['POST'])
def respAuth():
    if request.is_json:
        print(request.json)
        content=request.get_json()
        if content['login']==content['password']:
            content['token']='toto'
    return jsonify(content)

@app.route('/doc', methods=['POST'])
def respRes():
    if request.is_json:
        print(request.json)
        content=request.get_json()
        content['name']="tintin au tibet"
        content['author']="Herge"
        content['date']="1960"
        content[ 'type']='BD'
        content['id']='BDT9H2'
    return jsonify(content)