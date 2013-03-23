from config import OAUTH_SECRET, OAUTH_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
from twitter import *


twitterAPI = Twitter(
    auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
               CONSUMER_KEY, CONSUMER_SECRET))


x = twitterAPI.statuses.home_timeline()
print x[0]['user']['screen_name'] + ':' + x[0]['text']



