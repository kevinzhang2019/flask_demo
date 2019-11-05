from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    title = "web app"
    sentences = [
        "sentence 1",
        "sentence 2",
        "sentence 3",
        "sentence 4"
    ]
    return render_template("index.html", title=title, data=sentences)


if __name__ == '__main__':
    app.run(debug="True")
