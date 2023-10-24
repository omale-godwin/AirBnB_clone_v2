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


@app.route('/hbnb_filters', strict_slashes=False)
def get_filters():
    """ Returns all states, cities, and amenities."""
    states = storage.all('State').values()
    states = sorted(states, key=lambda state: state.name)
    amenities = storage.all('Amenity').values()
    amenities = sorted(amenities, key=lambda amenity: amenity.name)
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
