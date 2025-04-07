from flask import Flask, render_template
from api import API


app = Flask(__name__)
api = API()


@app.route("/")
def home():
    posts = api.get_posts()
    print(f"posts => {posts}")
    return render_template("index.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<post_id>")
def post(post_id):
    post = api.get_post_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return "Post not found", 404


if __name__ == "__main__":
    app.run(debug=True)
