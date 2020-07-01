from flask import (flash,
                   Flask,
                   jsonify,
                   make_response,
                   render_template,
                   request,
                   redirect,
                   url_for)
from flask import session as login_session
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import json
import requests
import urllib

SECRETS_JSON = json.loads(open(
    'C:\\Users\\Chris\\Documents\\mo_grits\\static\\secrets.json',
    'r')
    .read())

# Create instance of Flask class, and use name of running application.
app = Flask(__name__)

# Set secret_key variable.
app.secret_key = "1!2@3#4$"

# Create session and connect to database.
params = urllib.parse.quote_plus(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "Server=tcp:bchristopher.database.windows.net,1433;"
    "Database=mogrits;"
    "Uid=" + SECRETS_JSON['db']['Uid'] + ";"
    "Pwd=" + SECRETS_JSON['db']['Pwd'] + ";"
    "Encrypt=yes;"
    "TrustServerCertificate=no;"
    "Connection Timeout=30;"
)
engine = create_engine(
    "mssql+pyodbc:///?odbc_connect={}".format(params)
)
Base = automap_base()
Base.prepare(engine, reflect=True)
DBSession = sessionmaker(bind=engine)

Menu = Base.classes.menu
Period = Base.classes.period

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


@app.route('/about')
def showAbout():
    '''Return about.html template.

    Args:
        None

    Returns:
        'about.html' template.
    '''
    return render_template('about.html')


@app.route('/locations')
def showLocations():
    '''Return locations.html template.

    Args:
        None

    Returns:
        'locations.html' template.
    '''
    return render_template('locations.html')


@app.route('/menu/<int:period_id>', methods=['GET'])
def readMenu(period_id):
    '''

    '''
    session = DBSession()
    items = session.query(Menu).filter(Menu.period_id == period_id).all()
    menu_dict = {}
    menu_list = []
    for item in items:
        menu_list.append({"name": item.name, "description": item.description, "price": str(item.price)})
    menu_dict["period"] = menu_list
    return menu_dict


if __name__ == '__main__':
    app.run(debug=True)
