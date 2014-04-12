import json, urllib, urllib2, oauth2
from whatsforlunch.localsettings import CONSUMER_KEY, CONSUMER_SECRET, TOKEN_SECRET, TOKEN


def api_request(url_params, path='/v2/search'):
    """
    Returns response for API request.
    """
    consumer_key = CONSUMER_KEY
    consumer_secret = CONSUMER_SECRET
    token = TOKEN
    token_secret = TOKEN_SECRET

    host = 'api.yelp.com'

    encoded_params = ''

    if url_params:
        encoded_params = urllib.urlencode(url_params)
    url = 'http://{}{}?{}'.format(host, path, encoded_params)

    # Sign the URL
    consumer = oauth2.Consumer(consumer_key, consumer_secret)
    oauth_request = oauth2.Request('GET', url, {})
    oauth_request.update({'oauth_nonce': oauth2.generate_nonce(),
                    'oauth_timestamp': oauth2.generate_timestamp(),
                    'oauth_consumer_key': consumer_key})

    token = oauth2.Token(token, token_secret)
    oauth_request.sign_request(oauth2.SignatureMethod_HMAC_SHA1(), consumer, token)
    signed_url = oauth_request.to_url()

    # Connect
    try:
        conn = urllib2.urlopen(signed_url, None)

        try:
            response = json.loads(conn.read())
        finally:
            conn.close()

    except urllib2.HTTPError, error:
        response = json.loads(error.read())

    return response
