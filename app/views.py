"""
The general views for the music queue and webapp
"""
from app import app


@app.route('/health/')
def healthcheck():
    """ Endpoint to make sure the webapp is healthy """
    return 'Healthy\n', 200


@app.route('/api/message/')
def listen_for():
    """ Where all incoming messages will be processed"""
    pass
