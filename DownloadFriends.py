# Downloads list of people I follow in tw and puts it into a csv

import tweepy
import time
import csv
from datetime import datetime

from dotenv import load_dotenv
load_dotenv()

import os

consumer_key= os.getenv("consumer_key")
consumer_secret= os.getenv("consumer_secret")
access_token= os.getenv("access_token")
access_token_secret= os.getenv("access_token_secret")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

public_tweets = api.home_timeline()

friends=[]
def limit_handled(cursor):
    while True:
        try:
            yield next(cursor)
        except tweepy.RateLimitError:
            time.sleep(2 * 60)

for friend in limit_handled(tweepy.Cursor(api.friends).items()):
    friends.append(friend)

output=[]
for friend in friends:
    row=[]
    row.append(friend.id_str)
    row.append(friend.name)
    row.append(friend.screen_name)
    row.append(friend.location)
    row.append(friend.description)
    row.append(friend.url)
    row.append(friend.protected)
    row.append(friend.followers_count)
    row.append(friend.friends_count)
    row.append(friend.created_at)
    row.append(friend.geo_enabled)
    row.append(friend.verified)
    row.append(friend.following)
    output.append(row)

len(output)

now = datetime.now() # current date and time
#date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
date_time = now.strftime("%m%d%Y %H%M%S")
name="Out - "+date_time+".csv"
open(name, 'a').close()

with open(name, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(output)