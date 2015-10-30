# coding=utf-8

from lakers import app
"""
    Just examples for url mapping on using @app.route
"""
@app.route("/Los_Angeles/")
def los_angeles():
    return "Here is Los Angeles!"