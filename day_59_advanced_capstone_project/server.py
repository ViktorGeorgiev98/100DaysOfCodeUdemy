from flask import Flask, render_template
from api import API
from flask import request


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


@app.route("/post/<post_id>")
def post(post_id):
    post = api.get_post_by_id(post_id)
    if post:
        return render_template("post.html", post=post)
    else:
        return "Post not found", 404


@app.route("/contact", methods=["POST", "GET"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone")
        message = request.form.get("message")
        return f"Received message from {name} ({email}) with phone {phone}: {message}"
    return render_template("contact.html")
    # return render_template("contact.html", success=True)


if __name__ == "__main__":
    app.run(debug=True)
