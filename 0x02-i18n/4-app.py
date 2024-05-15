#!/usr/bin/env python3
'''A simple flask app'''


from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    '''Configure available languages'''

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


# configure the app
app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
app.url_map.strict_slashes = False

# This function is called by Flask-Babel to determine which language to use.
# It uses the Accept-Language header from the request to find the best match
# among the available languages.
@babel.localeselector
def get_locale() -> str:
    """
    Select the best match among the available languages based on the
    Accept-Language header of the request.

    Returns:
        The language code for the selected language.
    """
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        print(locale)
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index() -> str:
    """
    Render the index template.

    Returns:
        The rendered template as a string.
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000", debug=True)
