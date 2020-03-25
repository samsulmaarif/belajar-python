from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, flask!"

@app.route("/samsul")
def samsul():
    return "Hallo, samsul!"

@app.route("/admin/<string:name>")
def admin(name):
    name = name.capitalize()
    return f"<h1>Hello, admin {name}!</h1>"