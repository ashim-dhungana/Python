from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def main():
    return render_template('jinja.html')

app.run(debug=True)