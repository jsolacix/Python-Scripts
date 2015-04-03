from rauth import OAuth1Service

# Get a real consumer key & secret from https://dev.twitter.com/apps/new
twitter = OAuth1Service(
    name='twitter',
    consumer_key='vjvlBnuNmtNFjVloqB9MOxtrV',
    consumer_secret='UiYzaUwy3VXQDyqHZWwwj5mWKzwcDW36qfIcY1CXGrYTEmHTCz',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    base_url='https://api.twitter.com/1.1/')

request_token, request_token_secret = twitter.get_request_token()
print ("RT " + request_token)
print ("RTS " + request_token_secret)
authorize_url = twitter.get_authorize_url(request_token)

print 'Visit this URL in your browser: ' + authorize_url
pin = raw_input('Enter PIN from browser: ')  # `input` if using Python 3!

session = twitter.get_auth_session(request_token,
                                   request_token_secret,
                                   method='POST',
                                   data={'oauth_verifier': pin})

print ("AT " + session.access_token)
print ("ATS " + session.access_token_secret)

params = {'include_rts': 1,  # Include retweets
          'count': 10}       # 10 tweets

r = session.get('statuses/home_timeline.json', params=params)

for i, tweet in enumerate(r.json(), 1):
    handle = tweet['user']['screen_name']
    text = tweet['text']
    print(u'{0}. @{1} - {2}'.format(i, handle, text))
