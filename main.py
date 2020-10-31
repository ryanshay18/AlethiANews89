# https://flask.palletsprojects.com/en/1.1.x/api/
from flask import Flask, render_template

# create a Flask instance
app = Flask(__name__)


# connects default URL of server to a python function
@app.route('/')
def home():
    # function use Flask import (Jinga) to render an HTML template
    return render_template("home.html")


if __name__ == "__main__":
    # runs the application on the repl development server
    app.run(debug=True)
