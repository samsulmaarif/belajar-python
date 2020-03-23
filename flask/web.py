from flask import Flask, render_template
import datetime


app = Flask(__name__)

@app.route("/")
def index():
    headline = "Hello, Flask!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/newyear")
def newyear():
    now = datetime.datetime.now()
    new_year = now.month == 1 and now.day == 1
    return render_template("newyear.html", headline=new_year)