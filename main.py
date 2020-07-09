from flask import (flash,
                   Flask,
                   jsonify,
                   make_response,
                   render_template,
                   request,
                   redirect,
                   url_for)
from flask import session as login_session
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import sessionmaker

import json
import os
import requests
import sqlalchemy
import urllib

# Create public variable for secrets.
SECRETS_JSON = json.loads(open('./static/secrets.json', 'r').read())

# Create instance of Flask class, and use name of running application.
app = Flask(__name__)

# Set secret_key variable.
app.secret_key = "1!2@3#4$"

pool = sqlalchemy.create_engine(
    sqlalchemy.engine.url.URL(
        "mssql+pyodbc",
        username=SECRETS_JSON['db']['Uid'],
        password=SECRETS_JSON['db']['Pwd'],
        database="mogrits",
        host="35.231.209.191",
        port="1433",
        query={"driver": "ODBC Driver 17 for SQL Server"},
    ),
    pool_size=5,
    max_overflow=2,
    pool_timeout=30,
    pool_recycle=1800,
    echo=True
)

Base = automap_base()
Base.prepare(pool, reflect=True)
DBSession = sessionmaker(bind=pool)

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

# App route for about page uri.
@app.route('/about')
def showAbout():
    '''Return about.html template.

    Args:
        None

    Returns:
        'about.html' template.
    '''
    return render_template('about.html')

# App route for locations page uri.
@app.route('/locations')
def showLocations():
    '''Return locations.html template.

    Args:
        None

    Returns:
        'locations.html' template.
    '''
    return render_template('locations.html')

# App route for menu data uri.
@app.route('/menu/<int:period_id>', methods=['GET'])
def readMenu(period_id):
    '''Return dictionary of menu item list.

    Args:
        period_id - integer of breakfast, lunch or dinner period.

    Returns:
        menu_dict - dictionary of lists
    '''
    try:
        # Create new instance of DBSession.
        session = DBSession()

        # Use session to query database and return as list.
        items = session\
            .query(Menu)\
                .filter(Menu.period_id == period_id)\
                    .all()

        # Create dictionary and list variables.
        menu_dict = {}
        menu_list = []

        # Loop through items list, and append to menu_list.
        for item in items:
            menu_list.append(
                {
                    "name": item.name,
                    "description": item.description,
                    "price": str(item.price)
                }
            )

        # Add menu_list to menu_dict.
        menu_dict["period"] = menu_list

        # Close instance of DBSession.
        session.close()

        # Return menu_dict to client.
        return menu_dict

    except Exception as e:
        # Rollback instance of DBSession.
        session.rollback()

        # Print Exception.
        print(e)

    finally:

        # Close instance of DBSession.
        session.close()


# Used only for local development.
if __name__ == '__main__':
    app.run(debug=True)
