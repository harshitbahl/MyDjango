# -*- coding: utf-8 -*-
"""
Created on Tue Apr 29 23:46:39 2014

@author: harshitbahl
"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "This is very Nice test bro"

if __name__ == "__main__":
    app.run(host='0.0.0.0')