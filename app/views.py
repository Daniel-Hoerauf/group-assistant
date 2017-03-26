"""
The general views for the music queue and webapp
"""
from app import app
from .utils import get_env_var
from assistant import process
from flask import Response, request


@app.route('/health/')
def healthcheck():
    """ Endpoint to make sure the webapp is healthy """
    return 'Healthy\n', 200


@app.route('/api/message/', methods=['POST'])
def listen_for():
    """ Where all incoming messages will be processed"""
    bot_id = get_env_var('BOT_ID')
    process(request.json, bot_id)
    return Response(response='Message Received', status=200)
