#!/usr/bin/env python3
'''A simple flask app'''


from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config(object):
    '''Configure available languages'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


babel = Babel()


def get_locale() -> str:
    """
    Select the best match among the available languages based on the
    Accept-Language header of the request.

    Returns:
        The language code for the selected language.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)
babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index() -> str:
    """
    Render the index template.

    Returns:
        The rendered template as a string.
    """
    return render_template('2-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
