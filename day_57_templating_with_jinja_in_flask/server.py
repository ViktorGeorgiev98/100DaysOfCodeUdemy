from flask import Flask, render_template
import random
import time
import requests


def get_gender(name):
    response = requests.get(f"https://api.genderize.io?name={name}")
    return response.json()["gender"]


def get_age(name):
    response = requests.get(f"https://api.agify.io?name={name}")
    return response.json()["age"]


def get_blogs_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    blogs = response.json()
    return blogs


app = Flask(__name__)


@app.route("/")
def home():
    random_number = random.randint(1, 10)
    current_year = time.localtime().tm_year
    return render_template(
        "index.html", random_number=random_number, current_year=current_year
    )


@app.route("/guess/<name>")
def guess(name):
    gender = get_gender(name)
    age = get_age(name)
    return render_template("guess.html", name=name.title(), gender=gender, age=age)


@app.route("/blogs/<num>")
def get_blogs(num):
    print(num)
    blogs = get_blogs_posts()
    return render_template("blog.html", blogs=blogs)


if __name__ == "__main__":
    app.run(debug=True)
