# -*- coding: utf-8 -*-
"""
Created on Fri April  3 2020
"""

from flask import Flask
from config import Config
from flask_bootstrap import Bootstrap  # To use bootstrap styles

app = Flask(__name__)

app.config.from_object(Config)
app.static_folder = 'static'

bootstrap = Bootstrap(app)


from app import routes
