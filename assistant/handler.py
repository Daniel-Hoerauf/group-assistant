'''
A file
'''
import requests
from . import fn_map


def process(msg_json, bot_id):
    '''
    Check the response against the functionality and send a message to the group
    if needed
    '''
    first_word = msg_json['text'].split(' ')[0]
    remaining = msg_json['text'][len(first_word):]
    call = fn_map.get(first_word)
    if call:
        result = call(remaining)
        api = {
            'bot_id': bot_id,
            'text': result
        }
        req = requests.post('https://api.groupme.com/v3/bots/post', data=api)
    return None
