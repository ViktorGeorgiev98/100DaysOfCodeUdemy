from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    username = request.form.get("name")
    password = request.form.get("password")
    if not username or not password:
        raise Exception("Please fill in all fields")
    return f"Username: {username}, Password: {password}"


if __name__ == "__main__":
    app.run(debug=True)
