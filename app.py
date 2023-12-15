import flask
import subprocess

app = flask.Flask(__name__)


@app.route("/")
def index():
    return flask.render_template("home.html")


@app.route("/", methods=["POST"])
def process_form():
    # start = flask.request.form.get("start", "")

    # if start:
    command = "/usr/bin/toolforge jobs run mvn11 --image python3.9 --command \\\"python3 core8/pwb.py mvn/mvnew\\\""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return flask.render_template("home.html", result=result.stdout)
