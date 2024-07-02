#!/usr/bin/env python3

"""Module for starting babel app and getting local languages"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """Configuration class for setting up available languages and
       default settings."""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# Instantiate the Flask application
app = Flask(__name__)
app.config.from_object(Config)

# Instantiate the Babel object and bind it to the Flask app
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Determine the best match for supported languages."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/', strict_slashes=False)
def index():
    """Route for the index page which renders the 1-index.html template."""
    return render_template('1-index.html')


if __name__ == '__main__':
    # Run the Flask app on host 0.0.0.0 and port 5000
    app.run(host='0.0.0.0', port=5000)
