#!/usr/bin/env python3
""" A simple flask app """


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """_summary_
    """
    return render_template('0-index.html')
