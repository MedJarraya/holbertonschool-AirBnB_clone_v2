#!/usr/bin/python3
"""
starts a Flask web application module @author: @medjarraya
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hbnb():
    """
        fn to display Hello HBNB!
        in the route page
    """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
