#!/usr/bin/python3
"""A simple Flask application"""
from flask import Flask

# Create a Flask web application
app = Flask(__name__)


# Define a route for the root URL ("/") with strict_slashes=False
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a friendly HTTP greeting."""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
