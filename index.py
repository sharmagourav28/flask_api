# CRUD operation using REST API [ using Flask ] in Python

from flask import Flask, jsonify, request

app = Flask(__name__)

books = [
    {"id": 1, "title": "Mastering Python", "cost": 600},
    {"id": 2, "title": "Inside MySQL", "cost": 500},
    {"id": 3, "title": "Mastering Java", "cost": 800},
    {"id": 4, "title": "Machine Learning in details", "cost": 900},
]


@app.route("/books", methods=["GET"])
def get_books():
    return jsonify(books)


@app.route("/book/<int:book_id>", methods=["GET"])
def get_book(book_id):
    for book in books:
        if book["id"] is book_id:
            return jsonify(book)
    return jsonify({"error": "Book not found"})


@app.route("/book", methods=["POST"])
def add_book():
    new_book = {
        "id": request.json["id"],
        "title": request.json["title"],
        "cost": request.json["cost"],
    }
    books.append(new_book)
    return jsonify({"message": "Book has been added successfully"})


@app.route("/book/<int:book_id>", methods=["PUT"])
def modify_book(book_id):
    for book in books:
        if book["id"] is book_id:
            book["title"] = request.json["title"]
            book["cost"] = request.json["cost"]
            return jsonify({"message": "Book has been updated successfully"})
    return jsonify({"message": "Book not found"})


@app.route("/book/<int:book_id>", methods=["DELETE"])
def delete_book(book_id):
    for book in books:
        if book["id"] is book_id:
            books.remove(book)
            return jsonify({"message": "Book has been deleted successfully"})
    return jsonify({"message": "Book not found"})


# this is to start the server
if __name__ == "__main__":
    app.run(debug=True)
