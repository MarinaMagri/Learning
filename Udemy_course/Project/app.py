from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask_sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from datetime import datetime 

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///blog2.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"]="Key"
db = SQLAlchemy(app)
admin = Admin(app)

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


class CategoryView(ModelView):
    create_modal = True
    column_list = ("id","name", "articles")


class ArticleView(ModelView):
    create_modal = True
    column_list = ("id", "title", "introduction","pub_date")


admin.add_view(CategoryView(Category, db.session))
admin.add_view(ArticleView(Article, db.session))



@app.route("/")
def main():

    latest_articles = Article.query.order_by(Article.pub_date.desc())[:3]

    return render_template("index.html", articles = latest_articles)


@app.route("/blog")
def blog():
    category = Category.query.filter_by(name="Blog").first()
    articles = Article.query.filter_by(category_id=category.id)

    return render_template("blog.html", articles=articles)


@app.route("/news")
def news():
    category = Category.query.filter_by(name="News").first()
    articles = Article.query.filter_by(category_id=category.id)

    return render_template("news.html", articles=articles)


@app.route("/new_post", methods = ["GET", "POST"])
def new_post():
    if request.method == "POST":
        category_id = request.form["category_select"]
        title = request.form["title"]
        introduction = request.form["introduction"]
        text = request.form["article_text"]

        article = Article(category_id = category_id,
                          title = title,
                          introduction = introduction,
                          text = text)
        try:
            db.session.add(article)
            db.session.commit()

            return redirect(url_for("main"))

        except Exception as error:
            return f" Error: {error}"
    else:
        category = Category.query.all()
        return render_template("new_post.html", categories = category)

    
@app.route("/edit/<int:article_id>", methods = ["GET", "POST"])
def edit_post(article_id, previous = 'main'):
    article = Article.query.get_or_404(article_id)
    if request.method == "POST":
        previous = request.args.get('previous')
        article.category_id=request.form["category_select"]
        article.title=request.form["title"]
        article.introduction=request.form["introduction"]
        article.text=request.form["article_text"]

        try:
            db.session.commit()
            return redirect(url_for(previous))
        except Exception as error:
            return f" Error: {error}"

    else:
        category = Category.query.all()

    return render_template("edit_post.html", article=article, categories=category, previous=previous)



@app.route("/detailed_post/<int:article_id>")
def detailed_post(article_id):
    article = Article.query.get_or_404(article_id)

    return render_template("detailed.html", article = article)


@app.route("/delete_post <int:article_id>")
def delete_post(article_id):
    article = Article.query.get_or_404(article_id)

    try:
        db.session.delete(article)
        db.session.commit()

        return redirect(url_for("main"))

    except Exception as error:
        return f" Error: {error}"

        
if __name__ == "__main__":
    app.run(debug=True)