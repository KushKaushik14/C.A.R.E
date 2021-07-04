from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/health")
def health():
    return render_template("cool.html")
@app.route("/input")
def input():
    return render_template("input.htm")
@app.route("/hi")
def hi():
    return render_template("intheput.html")
@app.route("/")
def real():
    return render_template("header.html")
@app.route("/bot")
def bot():
    return render_template("bot.html")

