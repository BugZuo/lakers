# coding=utf-8

from lakers import app

from flask import render_template

"""
    Just examples for url mapping on using @app.route
"""
@app.route("/Los_Angeles/", methods=['GET'])
def los_angeles():
    return render_template("los_angeles.html")