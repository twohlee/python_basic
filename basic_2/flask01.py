from flask import Flask, render_template, request

app = Flask(__name__)


# 페이지를 만듦 
@app.route("/")
def index():
    return "index page"

@app.route("/join")
def join():
    return "join page"


if __name__ == '__main__':
    app.run(debug=True)
 
