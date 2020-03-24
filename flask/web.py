from flask import Flask, render_template, request
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

@app.route("/form")
def form():
    return render_template("form.html")

@app.route("/out", methods=["POST"])
def form_out():
    name = request.form.get("name")
    return render_template("out.html", name=name)

@app.route("/out2", methods=["POST", "GET"])
def form_out2():
    if request.method == "GET":
        return "Please submit the form instead!"
    else:
        name = request.form.get("name")
        return render_template("out.html", name=name)