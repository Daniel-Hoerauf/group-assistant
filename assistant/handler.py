'''
A file
'''
from . import fn_map


def process(msg_json):
    '''
    Check the response against the functionality and send a message to the group
    if needed
    '''
    text = msg_json['text']
    call = fn_map.get(text.split(' ')[0])
    if call:
        return call(text)
    return None
