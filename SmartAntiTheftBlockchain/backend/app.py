from flask import Flask
from flask import render_template

from database import get_events

app = Flask(__name__)

@app.route("/")
def index():

    return render_template(
        "index.html"
    )

@app.route("/history")
def history():

    events = get_events()

    return render_template(
        "history.html",
        events=events
    )

if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )