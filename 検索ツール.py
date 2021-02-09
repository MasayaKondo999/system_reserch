#初起動時にはpip install を忘れないこと

import tweepy
import csv
import datetime

# 取得したAPIキー
consumer_key = '2NU4F8yPIfTVAXpSSaRZXmWcE'
consumer_secret = 'BMild4HNIbQJghLiK1Towz7TJ6gZLiZTlVY0BpAOOii3fciWsQ'
access_token = '1323787767470456832-5TSsMVDAGfq0i33Vxpyn5RI4S6CdV1'
access_token_secret = 'AOniW4WEbERrt97RvQMBpQImde5ofdIwcL3rqt82Cu3RV'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth ,  wait_on_rate_limit=True)


#日付指定、sinceがスタート、untilがエンド、sinceのほうが古い時間で指定すること

sinceDate = '2021-02-01_00:01:00_JST'
untilDate = '2021-02-01_09:43:00_JST'

#検索数指定（多くても時間をかければ大丈夫）

num = 10000

tweet_data = []

counter = 0 

for i in range(1) :
    for tweet in tweepy.Cursor(api.search, q = ('死ね') , lang='ja',since = sinceDate , until = untilDate ).items(num):
        if not "RT @" in tweet.text[0:4]: 

            date_t = str(tweet.created_at)

            dt1 = datetime.datetime(int(date_t[0:4]) , int(date_t[5:7]) , int(date_t[8:10]) , int(date_t[11:13]) , int(date_t[14:16])) + datetime.timedelta(hours=9)

            tweet_data.append([tweet.id,dt1,tweet.text.replace('\n',''),tweet.favorite_count,tweet.retweet_count])
            counter = counter + 1


#出力データの名前、指定しないと同名で違うファイルが生成されるので注意

with open('C:\\Users\\184078\\Desktop\\VScode_desk\\CSVoutput_\\serch_output_as_2_1_nokori.csv', 'w',newline='',encoding='utf-8') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(["id","created_at","text","fav","RT"])
    writer.writerows(tweet_data)
pass

print("カウンターストップ　:" + str(counter) )
