from flask import render_template, flash, redirect, url_for, request
from app import app

from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/ConsumerView')
def ConsumerView():
    return render_template('ConsumerView.html', user = 1)

@app.route('/RetailerView')
def RetailerView():
    return render_template('RetailerView.html', user = 2)

@app.route('/ConsumerSavings')
def ConsumerSavings():
    return render_template('ConsumerSavings.html', user = 1)

@app.route('/ConsumerProducts')
def ConsumerProducts():
    return render_template('ConsumerProducts.html', user = 1)

@app.route('/RetailerHotProducts')
def RetailerHotProducts():
    return render_template('RetailerHotProducts.html', user = 2)

@app.route('/RetailerPredictions')
def RetailerPredictions():
    return render_template('RetailerPredictions.html', user = 2)

@app.route('/RetailerStore')
def RetailerStore():
    return render_template('RetailerStore.html', user = 2)


@app.route('/Dashboard01')
def Dashboard01():
    return render_template('Dashboard01.html', user = 2)
