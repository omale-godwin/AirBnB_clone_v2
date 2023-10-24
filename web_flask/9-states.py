#!/usr/bin/python3
"""A simple Flask application"""
from os import getenv
from flask import Flask, render_template

from models import storage

# Create a Flask web application
app = Flask(__name__)


@app.teardown_appcontext
def remove_current_session(exception):
    """ Removes the current SQLAlchemy session. """
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """ Renders a page with all states in the database."""
    states = storage.all('State')
    return render_template('9-states.html', state_obj=states)


@app.route('/states/<id>', strict_slashes=False)
def states_by_id(id: int):
    """ Renders a page with all cities by states in the database."""
    states = storage.all('State')
    for state in states.values():
        if state.id == id:
            return render_template('9-states.html', state_obj=state)

    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
