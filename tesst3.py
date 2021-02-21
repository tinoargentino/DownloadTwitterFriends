import tweepy

consumer_key='jxyk5BufAJUcGs4iB3Lzg5V7l'
consumer_secret='5TtFzcnZ2iXNPK5XCLYzSVaIUPbxp2NCR8pzU53hpYZ7jiwLtS'
access_token='346360426-3R934f0ZfOzo7FU4kZ47f2fiZhNN0jU9OEUBgKxF'
access_token_secret='y1PelClKQ9IaLPqw5ZqWkFyO7qT0ZOBux1vHl2LZp9h33'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

user = api.get_user('twitter')
print(user)