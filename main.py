import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv
import os

load_dotenv
API = os.getenv("API_KEY")

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("main.html")


@app.route("/result", methods=["POST"])
def results():
    movie = request.form['movie_name']
    url = f"http://www.omdbapi.com/?t={movie}&apikey={API}"
    content = requests.get(url)
    response = content.json()
    return render_template("results.html",  data=response)


app.run(debug=True, port=5000)