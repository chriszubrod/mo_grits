from flask import (flash, Flask, make_response, render_template,
                   request, redirect, url_for)
from flask import session as login_session

import json
import requests

# Create instance of Flask class, and use name of running application.
app = Flask(__name__)

# Set secret_key variable.
app.secret_key = "1!2@3#4$"

# App route for main and home page uri.
@app.route('/')
@app.route('/home')
def showHome():
    '''Return home.html template.

    Args:
        None

    Returns:
        'home.html' template.
    '''
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
