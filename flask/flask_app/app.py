"""
Example Flask app
"""

from flask import Flask

app = Flask(__name__)


@application.route("/")
def index():
    """
    Default route
    """
    return "Hello World!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
