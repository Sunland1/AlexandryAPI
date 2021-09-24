from flask import Flask, request, jsonify, Response
import model
import json


app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/book", methods=["GET", "POST"])
def book_all():
    if request.method == "GET":
        body, status = model.get_book_all()
        return body
    elif request.method == 'POST':
        new_book = request.json
        r_ok = model.add_book(new_book)
        return Response(status=r_ok)


@app.route("/book/<int:id_book>", methods=["GET", "PUT", "DELETE"])
def book(id_book):
    if request.method == "GET":
        book, status = model.get_book(id_book)
        return book
    elif request.method == "PUT":
        data_to_modify = request.json
        book, status = model.modify_book(data_to_modify, id_book)
        return book
    elif request.method == "DELETE":
        body, status = model.delete_book(id_book)
        return Response(status=status)
    else:
        return "test"

