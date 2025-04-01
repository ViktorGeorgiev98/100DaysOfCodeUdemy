# import flask
from flask import Flask

# Create a Flask application instance
# The first argument is the name of the application module or package.
app = Flask(__name__)


# Define a route for the root URL ("/")
@app.route("/")
def hello_world():
    return "Hello World!"


@app.route("/bye")
def say_bye():
    return "Bye!"


if __name__ == "__main__":
    # Run the application on the local development server
    # The debug=True option enables debug mode, which provides detailed error messages and auto-reloads the server on code changes.
    app.run(debug=True)
