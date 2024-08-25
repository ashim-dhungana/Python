from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('index2.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/post.html")
def post():
    return render_template('post.html')

@app.route("/image.html")
def image():
    return render_template('image.html')

app.run(debug=True)