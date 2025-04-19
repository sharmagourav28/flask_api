from flask import Flask, render_template, jsonify
import mysql.connector as m

# database connectivity

mydatabase = m.connect(
    host="localhost", user="root", password="Gourav@2806", database="pythondb1"
)
cursor = mydatabase.cursor()

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


@app.route("/persons", methods=["GET"])
def getPersons():
    query = "select * from person"
    cursor.execute(query)
    result = cursor.fetchall()
    print(result)
    return render_template("welcome.html", data=result)


if __name__ == "__main__":
    app.run(debug=True)
