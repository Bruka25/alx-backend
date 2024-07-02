#!/usr/bin/env python3

"""Module for initializing Flask app"""

from flask import Flask, render_template

# Instantiate the Flask application
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Route for the index page.

    This route renders the '0-index.html' template when accessed.
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
