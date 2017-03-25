'''
Utility functions
'''
from os import environ

def get_env_var(envvar):
    '''Get environment variable or exit'''
    var = environ.get(envvar)
    if var:
        return var
    exit(1)
