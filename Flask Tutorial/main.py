from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:database123@localhost:3306/flask_tutorial'

db = SQLAlchemy(app)


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    phone_num = db.Column(db.String(12), nullable=False)
    email = db.Column(db.String(20), nullable=False)
    msg = db.Column(db.String(20), nullable=False)

class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(30), nullable=False)
    content = db.Column(db.String(500), nullable=False)


@app.route("/")
def main():
    return render_template('index.html')


@app.route("/index.html")
def home():
    return render_template('index.html')


@app.route("/about.html")
def about():
    return render_template('about.html')


@app.route("/contact.html", methods = ['GET','POST'])
def contact():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        entry = Contacts(name=name, phone_num=phone, msg=message, email=email)

        db.session.add(entry)
        db.session.commit()

    return render_template('contact.html')


@app.route("/post.html")
def post():
    return render_template('post.html')


@app.route("/image.html")
def image():
    return render_template('image.html')


app.run(debug=True)