from flask import Flask
import random


def random_number():
    return random.randint(0, 9)


home_page_html = "<h1>Guess a number between 0 and 9</h1>\n<img src='https://media4.giphy.com/media/12Ge3LuCAofm2A/giphy.webp?cid=790b76115mexentmqkvba55bmze7suyykr4cnnv4iuc10jad&ep=v1_gifs_trending&rid=giphy.webp&ct=g' />"


app = Flask(__name__)


@app.route("/")
def home_page():
    return home_page_html


@app.route("/<int:number>")
def guess_number(number):
    if number == random_number():
        return "<h1 style='color: green'>You found me!</h1>"
    elif number < random_number():
        return "<h1 style='color: red'>Too low, try again!</h1>"
    else:
        return "<h1 style='color: blue'>Too high, try again!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
