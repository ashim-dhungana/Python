from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/new")
def new():
    return "This is a new page"

app.run()
app.run(debug=True)