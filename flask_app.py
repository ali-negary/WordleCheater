from flask import Flask

app = Flask(__name__)


@app.route("/home")
def index():
    return "In case you did not notice, this is the Homepage."


if __name__ == "__main__":
    app.run(debug=True)
