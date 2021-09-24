from flask import Flask,request,jsonify


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/book" , methods=["GET","POST"] )
def bookAll() : 
    return -1




@app.route("/book/<int:id_book>" , methods=["GET","PUT","DELETE"] )
def book(id_book) : 
    if request.method == "GET" : 
        return {}
    elif request.method == "PUT" :
        data_to_modify = jsonify(request.json)
        return {}
    elif request.method == "DELETE" :
        return {}
    else : 
        return "test"


