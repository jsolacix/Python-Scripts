import requests
from requests_oauthlib import OAuth1

url = 'https://api.twitter.com/1.1/statuses/update.json'
url2 = 'https://api.twitter.com/1.1/statuses/home_timeline.json'  
#url3 = 'https://uploadtwitter.com/1.1/media/upload.json'
auth =OAuth1('vjvlBnuNmtNFjVloqB9MOxtrV', 'UiYzaUwy3VXQDyqHZWwwj5mWKzwcDW36qfIcY1CXGrYTEmHTCz', '3131508861-fZI0jZkmLejHR8E9w36Vhc6QLTzszEPCIf2iMDh', 'C3NOgS5VRgeEQFb7xGMWkzY3PDfEY6rRQHVICA55V5JAD')
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
