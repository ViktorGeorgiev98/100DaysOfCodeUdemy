from flask import Flask, render_template
import requests


def get_posts():
    response = requests.get("https://api.npoint.io/c790b4d5cab58020d391")
    posts = response.json()
    return posts


app = Flask(__name__)


@app.route("/")
def home():
    posts = get_posts()
    return render_template("index.html", posts=posts)


@app.route("/post/<id>")
def get_post(id):
    posts = get_posts()
    current_post = None
    for post in posts:
        if post["id"] == int(id):
            current_post = post
    return render_template("post.html", post=current_post)


if __name__ == "__main__":
    app.run(debug=True)
