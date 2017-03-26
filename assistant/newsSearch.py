import http.client, urllib.request, urllib.parse, urllib.error, base64
from os import getenv

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': getenv('BING_SEARCH'),
}

params = urllib.parse.urlencode({
    # Request parameters
    'q': 'bernie',
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
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))