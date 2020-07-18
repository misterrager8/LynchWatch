from flask import Flask, render_template

from classes import ctrla

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html", sc=ctrla.Ctrla())


@app.route("/info")
def info_page():
    return render_template("info.html")


@app.route("/contact")
def contact_page():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)
