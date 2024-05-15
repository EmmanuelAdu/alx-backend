#!/usr/bin/env python3
'''A simple flask app'''


from flask import Flask, render_template, request, g
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

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

def get_user():
    '''Returns a dictionary of users'''
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None

@app.before_request
def before_request() -> None:
    """_summary_
    """
    user = get_user()
    g.user = user


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
