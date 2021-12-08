# Flask aplikacija 02
# pip install -r requirements.txt

from flask import Flask
from flask.templating import render_template

app= Flask(__name__)

@app.route("/")
def index():
    poruka="Ovo je poruka iz main.py"
    return render_template("index.html", poruka=poruka)

@app.route("/onama")
def onama():
    return render_template("onama.html")

if __name__== "__main__":
    app.run(use_reloader= True)