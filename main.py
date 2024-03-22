from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Float

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
#app
app = Flask(__name__)

#create database
class Base(DeclarativeBase):
  pass

#configure the extension
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///books.db"
db = SQLAlchemy(model_class=Base)
db.init_app(app)

#create table
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(40), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(40), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

#create schema
with app.app_context():
    db.create_all()

#create home page
@app.route('/')
def home():
    list = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = list.scalars()
    return render_template("index.html", books=all_books)

#create add page
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home'))
    
    return render_template("add.html")

@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_update = db.get_or_404(Book, book_id)
        book_update.rating = request.form["rating"]
        db.session.commit()

        return redirect(url_for("home"))
    
    book_id = request.args.get("id")
    book = db.get_or_404(Book, book_id)

    return render_template("edit.html", book=book)

@app.route("/delete")
def delete():
    book_id = request.args.get("id")

    book_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_delete)
    db.session.commit()    

    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)