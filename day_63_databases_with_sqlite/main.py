from flask import Flask, render_template, request, redirect, url_for
from db import DB

"""
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
"""

app = Flask(__name__)
db = DB()
# db.create_table()


@app.route("/")
def home():
    books = db.get_all()
    print(books)
    return render_template("index.html", books=books)


@app.route("/add", methods=["POST", "GET"])
def add():
    if request.method == "POST":
        db.add_row(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"],
        )
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/delete/<int:id>")
def delete(id):
    db.cursor.execute("DELETE FROM books WHERE id=?", (id,))
    db.db.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
