from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Category(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False, unique = True)
    articles = db.relationship("Article", backref = "category_name")

    def __repr__(self):
        return f"Category: {self.id} - {self.name}"

class Article(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"))
    title = db.Column(db.String(50), nullable = False, unique = True)
    introduction = db.Column(db.String(100), nullable = False)
    text = db.Column(db.Text(), nullable = False)
    pub_date = db.Column(db.DateTime, default = datetime.utcnow)


def __repr__(self):
    return f"Article: {self.id} - {self.title}"

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