# -*- coding: utf-8 -*-
"""
Created on Fri April  3 2020
"""

from flask import Flask

app = Flask(__name__)

from app import routes
