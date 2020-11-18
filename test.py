import tweepy
# 取得したAPIキー
consumer_key = '2NU4F8yPIfTVAXpSSaRZXmWcE'
consumer_secret = 'BMild4HNIbQJghLiK1Towz7TJ6gZLiZTlVY0BpAOOii3fciWsQ'
access_token = '1323787767470456832-5TSsMVDAGfq0i33Vxpyn5RI4S6CdV1'
access_token_secret = 'AOniW4WEbERrt97RvQMBpQImde5ofdIwcL3rqt82Cu3RV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




for tweet in tweepy.Cursor(api.search, q='スマブラ').items(100):
    print(tweet)

