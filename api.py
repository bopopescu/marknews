import flask, requests, jsonify
from flask import render_template, request
from getters import * 

app = flask.Flask(__name__)
app.config["DEBUG"] = True

#TESTING
company = "google"
ticker = "goog"

@app.route('/news', methods=['GET'])
def news():
    news = get_news_json(company)
    return news

@app.route('/scores', methods=['GET'])
def scores():
    return scores

@app.route('/stocks', methods=['GET'])
def stocks():
    return stocks

@app.errorhandler(404)
def page_not_found(e):
    return "<center><h1>404</h1><p>This page could not be found.</p></center>", 404

app.run()