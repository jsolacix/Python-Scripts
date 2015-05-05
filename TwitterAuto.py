from rauth import OAuth1Service

# Get a real consumer key & secret from https://dev.twitter.com/apps/new
twitter = OAuth1Service(
    name='twitter',
    consumer_key='',
    consumer_secret='',
    request_token_url='https://api.twitter.com/oauth/request_token',
    access_token_url='https://api.twitter.com/oauth/access_token',
    authorize_url='https://api.twitter.com/oauth/authorize',
    base_url='https://api.twitter.com/1.1/')

request_token = ''
request_token_secret = ''	

authorize_url = twitter.get_authorize_url(request_token)

print 'Login automatically'



access_token = ''
access_token_secret = ''

session = twitter.get_session((access_token, access_token_secret))


params = {'include_rts': 1,  # Include retweets
          'count': 10}       # 10 tweets

r = session.get('statuses/home_timeline.json', params=params)

for i, tweet in enumerate(r.json(), 1):
    handle = tweet['user']['screen_name']
    text = tweet['text']
    print(u'{0}. @{1} - {2}'.format(i, handle, text))

