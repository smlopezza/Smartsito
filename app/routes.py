from flask import render_template, flash, redirect, url_for, request
from app import app

from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse



@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
