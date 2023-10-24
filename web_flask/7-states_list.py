#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask, render_template

from models import storage

# Create a Flask web application
app = Flask(__name__)


@app.teardown_appcontext
def remove_current_session(exception):
    """ Removes the current SQLAlchemy session. """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_states():
    """ Renders a page with all states in the database. """
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
