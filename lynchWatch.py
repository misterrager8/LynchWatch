from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home_page():
    return render_template("index.html")


@app.route("/info")
def info_page():
    return render_template("info.html")


if __name__ == "__main__":
    app.run(debug=True)
