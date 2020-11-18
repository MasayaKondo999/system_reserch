import tweepy
# 取得したAPIキー
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = 'A'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




for tweet in tweepy.Cursor(api.search, q='k').items(100):
    print(tweet)

