from flask import Flask, render_template, request, redirect, url_for, flash, jsonify

app = Flask(__name__)


@app.route("/")
def home():
    return "In case you did not notice, this is the Homepage."


if __name__ == "__main__":
    app.run(debug=True)
