from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/test")
def something():
    l = [1,2,3,4,5]

    return render_template("test.html")


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/blog")
def blog():
    return render_template("blog.html")


@app.route("/news")
def news():
    return render_template("news.html")


if __name__ == "__main__":
    app.run(debug=True)