import flask
import subprocess

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("home.html")


@app.route("/", methods=["POST"])
def process_form():
    start = flask.request.form.get("start", "")

    if start:
        command = "jsub -N mvn11 python310 ./core8/pwb.py mvn/mvnew"
        result = subprocess.call(command, shell=True, capture_output=True, text=True)
        return flask.render_template("home.html", result=result)
