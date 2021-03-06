import tweepy
import csv

consumer_key=""
consumer_secret = ""
access_key= ""
access_secret = ""

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

q = "フリート"
count=5

tweet_list=[]

tweets = api.search(q=q, locale="ja", count=count,tweet_mode='extended')
for tweet in tweets:
    tweet_list.append([[tweet.user.id, tweet.user.followers_count,
                        tweet.user.friends_count, tweet.user.description],
                       [tweet.id, tweet.full_text, tweet.favorite_count, 
                        tweet.retweet_count]])

with open("Tweetsdata.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f,  lineterminator="\n")
    writer.writerow(tweet_list)
