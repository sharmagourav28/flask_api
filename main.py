from flask import Flask, render_template, jsonify


app = Flask(__name__, template_folder="template")  # using custom folder

books = [
    {"id": 1, "title": "Mastering Python", "cost": 600},
    {"id": 2, "title": "Inside MySQL", "cost": 500},
    {"id": 3, "title": "Mastering Java", "cost": 800},
    {"id": 4, "title": "Machine Learning in details", "cost": 900},
]


@app.route("/", methods=["GET"])
def getHome():
    print("Welcome Home")
    return render_template("home.html")


@app.route("/books", methods=["GET"])
def getBooks():
    return jsonify(books)


if __name__ == "__main__":
    app.run(debug=True)
