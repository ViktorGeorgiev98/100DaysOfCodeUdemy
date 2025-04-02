# import flask
from flask import Flask


def make_bold(func):
    def wrapper():
        return f"<b>{func()}</b>"

    return wrapper


def make_emphasis(func):
    def wrapper():
        return f"<em>{func()}<em/>"

    return wrapper


def make_underlines(func):
    def wrapper():
        return f"<u>{func()}<u/>"

    return wrapper


# Create a Flask application instance
# The first argument is the name of the application module or package.
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return (
        '<h1 style="text-align: center">Hello, World!</h1>'
        '<p style="text-align: center">This is my first Flask app</p>'
        '<img style="text-align: center, width: 100px" src="https://www.humaneworld.org/sites/default/files/styles/responsive_3_4_500w/public/2022-07/kitten-playing-575035.jpg.webp?itok=6JOrIuo1" /> '
    )


# different routes using the app.route decorator
@app.route("/bye")
@make_bold
@make_emphasis
@make_underlines
def say_bye():
    return "Bye!"


@app.route("/username/<username>/<int:number>")
def greet(username, number):
    return f"Hello, {username}, you are {number} years old!"


if __name__ == "__main__":
    # Run the application on the local development server
    # The debug=True option enables debug mode, which provides detailed error messages and auto-reloads the server on code changes.
    app.run(debug=True)
