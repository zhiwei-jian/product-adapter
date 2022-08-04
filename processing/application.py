# Copyright © 2016-2022 Dell Inc. or its subsidiaries.
# All Rights Reserved.

"""This module creates and starts a Flask web application and exposes the APIs for the audit service."""

from flask import Flask

from processing.controllers import product_controller

app = Flask(__name__)


def _initialization(flask_app):
    """Initializes base services at startup."""
    # Register with the discovery service.
    # app.run()



def run():
    """Runs the application."""
    product_controller.run()
    # app.run()