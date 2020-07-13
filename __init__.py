from flask import (flash,
                   Flask,
                   jsonify,
                   make_response,
                   render_template,
                   request,
                   redirect,
                   url_for)
from flask import session as login_session

import json
import pyodbc
import requests

# Create public variable for secrets.
SECRETS_JSON = json.loads(open('./static/secrets.json', 'r').read())

# Create instance of Flask class, and use name of running application.
app = Flask(__name__)

# Set secret_key variable.
app.secret_key = "1!2@3#4$"

def open_connection():
    conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};' + 
        'SERVER=tcp:bchristopher.database.windows.net,1433;' +
        'DATABASE=bchristopher_apps_db;UID=' + SECRETS_JSON['db']['Uid'] + ';' + 
        'PWD=' + SECRETS_JSON['db']['Pwd'] + ';' +
        'Encrypt=yes;' +
        'Connection Timeout=30;'
    )
    return conn

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
    with open_connection() as conn:
        try:
            cursor = conn.cursor()
            cursor.execute(
                '''
                SELECT name, description, price
                FROM menu
                WHERE period_id = {};
                '''.format(period_id)
            )

            # Create dictionary and list variables.
            menu_dict = {}
            menu_list = []

            # Loop through items list, and append to menu_list.
            for row in cursor:
                menu_list.append(
                    {
                        "name": row[0],
                        "description": row[1],
                        "price": str(row[2])
                    }
                )

            # Add menu_list to menu_dict.
            menu_dict["period"] = menu_list

            # Return menu_dict to client.
            return menu_dict

        except Exception as e:

            # Print Exception.
            print(e)


# Used only for local development.
if __name__ == '__main__':
    app.run(debug=True)
