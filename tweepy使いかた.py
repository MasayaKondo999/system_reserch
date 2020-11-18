#自分のアカウントのフォロワーをすべて取得する
api.followers_ids(userid) 


# 自分のアカウントがフォローしている人を取得
following_id = api.friends_ids(userid)
 

# フォロー（user_idはフォローする人のID）
api.create_friendship(user_id)


# 特定のユーザーのツイートを取得
for status in api.user_timeline(id=''):
    #見映えのため区切る
    print('-------------------------------------------')
    #ユーザ名表示
    print('name:' + status.user.name)
    #内容表示
    print(status.text)


# ファボ（いいね！）
api.create_favorite(tweet_id)


# ツイート検索
api.search(q=q, count=count)


# タイムライン取得
for status in api.home_timeline():
    #見映えのため区切る
    print('-------------------------------------------')
    #ユーザ名表示
    print('name:' + status.user.name)
    #内容表示
    print(status.text)


# 特定のユーザーのツイートを取得する
tweet_data = []
for tweet in tweepy.Cursor(api.user_timeline, screen_name="取得したいユーザーのアカウントID(例:@python_mllover)", exclude_replies=True).items():
    tweet_data.append([tweet.id, tweet.created_at, tweet.text.replace('\n', ''), tweet.favorite_count, tweet.retweet_count])
