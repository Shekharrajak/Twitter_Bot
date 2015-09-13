from twitter import Twitter, OAuth, TwitterHTTPError

OAUTH_TOKEN = '171006213-fwxpi1D1w6OrK8Ojwv7f1BboPBHvEVKq8m6lGSsq'
OAUTH_SECRET = 'K8CuGPfk5fXksUWMcudqXiIMtGvaF4Heb16phh9xXANRH'
CONSUMER_KEY = 'C69L0bwIsNd0ws42XkaloK1qA'
CONSUMER_SECRET = 'YkdbBUFa07jWQ2W6OV2oz3w7xMq7jSwYdWHhNjBigceWBdw9Dv'

t = Twitter(auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
            CONSUMER_KEY, CONSUMER_SECRET))

def search_tweets(q, count=100):
    return t.search.tweets(q=q, result_type='recent', count=count)

def fav_tweet(tweet):
    try:
        result = t.favorites.create(_id=tweet['id'])
        print "Favorited: %s" % (result['text'])
        return result
    # when you have already favourited a tweet
    # this error is thrown
    except TwitterHTTPError as e:
        print "Error: ", e
        return None

def auto_fav(q, count=100):
    result = search_tweets(q, count)
    a = result['statuses'][0]['user']['screen_name']
    print a
    success = 0
    for tweet in result['statuses']:
        if fav_tweet(tweet) is not None:
            success += 1
    print "We Favorited a total of %i out of %i tweets" % (success,
          len(result['statuses']))
