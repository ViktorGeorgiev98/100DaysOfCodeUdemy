from flask import Flask, render_template, request
from form import Form_Login

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
app.secret_key = "your-secret-key"  # Needed for CSRF protection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form_login = Form_Login()
    if request.method == "POST":
        if form_login.validate_on_submit():
            email = form_login.email.data
            password = form_login.password.data
            print(f"Form Data => {form_login.data}")
            print(f"Email: {email}, Password: {password}")
            return render_template("success.html", email=email)
        else:
            print(form_login.errors)
            print("Form not validated")
            return render_template("denied.html")
    return render_template("login.html", form=form_login)


if __name__ == "__main__":
    app.run(debug=True)
