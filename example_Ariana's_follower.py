
import tweepy
import csv

consumer_key=""
consumer_secret = ""
access_key= ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

#ツイート取得
tweet_data = []

for tweet in tweepy.Cursor(api.user_timeline,screen_name = "@ArianaGrande",exclude_replies = True).items():
    tweet_data.append([tweet.id,tweet.created_at,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])

#csv出力
with open('tweets_20170805.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
pass
