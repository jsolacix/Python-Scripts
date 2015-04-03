import requests
from requests_oauthlib import OAuth1, OAuth1Session
client_key='vjvlBnuNmtNFjVloqB9MOxtrV'
client_secret='UiYzaUwy3VXQDyqHZWwwj5mWKzwcDW36qfIcY1CXGrYTEmHTCz'
request_token_url='https://api.twitter.com/oauth/request_token'
access_token_url='https://api.twitter.com/oauth/access_token'
authorize_url='https://api.twitter.com/oauth/authorize'
callback_uri = 'https://127.0.0.1/callback'
oauth_session = OAuth1Session(client_key, client_secret=client_secret)
oauth_session.fetch_request_token(request_token_url)
full_autorize_url = oauth_session.authorization_url(authorize_url)
print 'Visit this URL in your browser: ' + full_autorize_url
verifier = raw_input('Enter PIN here: ')


oauth_session.parse_authorization_response(full_autorize_url)


access_token, access_token_secret = oauth_session.fetch_access_token(access_token_url, verifier)



url = 'https://api.twitter.com/1.1/statuses/update.json'
url2 = 'https://api.twitter.com/1.1/statuses/home_timeline.json'  
#url3 = 'https://uploadtwitter.com/1.1/media/upload.json'
auth =OAuth1(consumer_key, consumer_secret, access_token, access_token_secret)
params2 = {'include_rts': 1,  # Include retweets
          'count': 10}
message = raw_input('Enter a new twitt: ')
params = {'status': message,}
p = requests.post(url, auth=auth, params=params)
g = requests.get(url2, auth=auth, params=params2)
#media = request.post(url3, auth=auth, )
print p.json
print p.url
print g.json
print g.url
for i, tweet in enumerate(g.json(), 1):
    handle = tweet['user']['screen_name']
    text = tweet['text']
    print(u'{0}. @{1} - {2}'.format(i, handle, text)) 
