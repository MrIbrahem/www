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
    command = 'toolforge jobs run mvn11 --image python3.9 --command "python3 core8/pwb.py mvn/mvnew"'
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, env={"PATH": "/usr/bin"})
    return flask.render_template("home.html", result=result.stdout, co=command)


@app.route("/uu")
def start():
    command = "jobs.sh"
    result = subprocess.run(command, shell=True, capture_output=True, text=True, env={"PATH": "/usr/bin"})
    return flask.render_template("home.html", result=result.stdout, co=command)

@app.route("/jobs")
def jobs():
    command = 'toolforge jobs list'
    result = subprocess.call(command, shell=True, env={"PATH": "/usr/bin"})
    return flask.render_template("home.html", result=result, co=command)

@app.route("/ja")
def ja():
    command = 'toolforge jobs list'
    result = subprocess.run(command, shell=True, capture_output=True, text=True, env={"PATH": "/usr/bin"})
    return flask.render_template("home.html", result=result, co=command)
