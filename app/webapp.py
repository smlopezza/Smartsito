from flask import Blueprint, render_template, abort, flash, redirect, url_for, request
#from app import app
from app import create_app
from flask_bootstrap import Bootstrap

# Redirect to "next" page
from werkzeug.urls import url_parse

server_bp = Blueprint('main', __name__)


@server_bp.route('/')
@server_bp.route('/index')
def index():
    return render_template("index.html")

@server_bp.route('/ConsumerView')
def ConsumerView():
    return render_template('ConsumerView.html', user = 1)

@server_bp.route('/RetailerView')
def RetailerView():
    return render_template('RetailerView.html', user = 2)

@server_bp.route('/ConsumerSavings')
def ConsumerSavings():
    return render_template('ConsumerSavings.html', user = 1)

@server_bp.route('/ConsumerProducts')
def ConsumerProducts():
    return render_template('ConsumerProducts.html', user = 1)

@server_bp.route('/ConsumerRewards')
def ConsumerRewards():
    return render_template('ConsumerRewards.html', user = 1)

@server_bp.route('/RetailerHotProducts')
def RetailerHotProducts():
    return render_template('RetailerHotProducts.html', user = 2)

@server_bp.route('/RetailerPredictions')
def RetailerPredictions():
    return render_template('RetailerPredictions.html', user = 2)

@server_bp.route('/RetailerStore')
def RetailerStore():
    return render_template('RetailerStore.html', user = 2)


@server_bp.route('/Dashboard01')
def Dashboard01():
    return render_template('Dashboard01.html', user = 2)
