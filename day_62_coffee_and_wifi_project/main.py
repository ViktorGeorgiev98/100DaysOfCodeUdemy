from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
import csv
from wtforms.validators import ValidationError
import re

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
app.config["SECRET_KEY"] = "8BYkEfBA6O6donzWlSihBXox7C0sKR6b"
Bootstrap5(app)


# Custom Validator function to check if the URL starts with http:// or https://
def validate_google_maps_url(form, field):
    url = field.data
    print(f"Validating URL: {url}")  # Debugging output to check the URL

    # This regular expression ensures the URL starts with http:// or https://
    google_maps_pattern = r"^(https?://).*"  # Match http:// or https://

    # Print if regex matches
    if re.match(google_maps_pattern, url):
        print("URL is valid")
    else:
        print("URL is NOT valid")

    # Check if URL matches the pattern
    if not re.match(google_maps_pattern, url):
        raise ValidationError(
            "Please enter a valid URL starting with http:// or https://"
        )


# Form class definition
class CafeForm(FlaskForm):
    cafe = StringField("Cafe name", validators=[DataRequired()])
    location = StringField(
        "Location on Google Maps (URL)",
        validators=[DataRequired(), validate_google_maps_url],
    )
    cafe_rating = StringField("Cafe Rating", validators=[DataRequired()])
    submit = SubmitField("Submit")


# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
# e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        print("True")
        return redirect(url_for("cafes"))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    print("not submitted")
    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open(
        "day_62_coffee_and_wifi_project\cafe-data.csv", newline="", encoding="utf-8"
    ) as csv_file:
        csv_data = csv.reader(csv_file, delimiter=",")
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
        print(list_of_rows)
    return render_template("cafes.html", cafes=list_of_rows)


if __name__ == "__main__":
    app.run(debug=True)
