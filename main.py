from flask import Flask, jsonify  # jsonify remove the error

app = Flask(__name__)


@app.route("/", methods=["GET"])
def getHome():
    return "Welcome Home"


@app.route("/books", methods=["GET"])
def getBooks():
    booklist = ["Complete Reference Python", "Mastering Python", "Deep dive into MySQL"]
    return jsonify(booklist)  # added jsonify


if __name__ == "__main__":
    app.run(debug=True)
