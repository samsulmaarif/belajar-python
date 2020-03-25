from flask import Flask, render_template, request, sessions
from flask_sessions import sessions

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
# sessions(app)

notes = []

@app.route("/", methods=["GET", "POST"])
def index():
    # if sessions("notes") is None:
        # session["notes"] = []
    if request.method == "POST":
        note = request.form.get("note")
        session["notes"].append(note)
    return render_template("session.html", notes=notes)




