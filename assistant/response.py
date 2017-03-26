"""
All of the individual methods that the assistant has
"""
import subprocess
import random
import twitter
import sys
import http.client, urllib.request, urllib.parse, urllib.error, base64
from os import getenv

def answer(question):
    '''
    Will respond to any question with the best answer it can find
    '''
    ans = subprocess.Popen(['sirius.sh', question], stdout=subprocess.PIPE).stdout.read() 
    if(ans):
	    return ans
    else:
        return "No answers could be divined. Please try again"


def last_tweet(username):
    username = username.strip().split(' ')[0]
    key = getenv('CONSUMER_KEY')
    secret = getenv('SECRET_KEY')
    token = getenv('ACCESS_TOKEN')
    token_secret = getenv('ACCESS_SECRET')
    api = twitter.Api(consumer_key=key, consumer_secret=secret, access_token_key=token, access_token_secret=token_secret)
    response = api.GetUserTimeline(screen_name=username)[0]
    status_addr = 'https://twitter.com/{}/status/{}'.format(username, response.id)
    return status_addr

def eight_ball(options):
    '''s
    Given a list of quote enclosed options, will choose one
    '''
    choices = [ 'It is certain',
                'It is decidedly so',
                'Without a doubt',
                'Yes, definitely',
                'You may rely on it',
                'As I see it, yes',
                'Most likely',
                'Outlook good',
                'Signs point to yes',
                'Reply hazy try again',
                'Ask again later',
                'Better not to tell you now',
                'Cannot predict now',
                'Concentrate and ask again',
                'Don\'t count on it',
                'My reply is no',
                'My sources say no',
                'Outlook not so good',
                'Very doubtful'
                ]

    ans = random.choice(choices)
    return ans

def weather(city):
    proc = subprocess.Popen(['/home/ubuntu/group-assistant/assistant/weatherTest.py',  "'" + city.strip() + "'"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    return proc.communicate()[0]    

def math(expression):
    ans = eval(expression)
    if ans:
        return ans
    else:
        return 'That is some nasty math. Please try something else.'

def news(topic):
    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': getenv('BING_SEARCH'),
    }

    params = urllib.parse.urlencode({
        # Request parameters
        'q': topic,
        'count': '10',
        'offset': '0',
        'mkt': 'en-us',
        'safeSearch': 'Moderate',
    })

    try:
        conn = http.client.HTTPSConnection('api.cognitive.microsoft.com')
        conn.request("GET", "/bing/v5.0/news/search?%s" % params, "{body}", headers)
        response = conn.getresponse()
        data = response.read()
        return "Works!"
        conn.close()
    except Exception as e:
        return "SAD!"
