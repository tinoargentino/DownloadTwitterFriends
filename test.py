from twitter import *

consumer_key='jxyk5BufAJUcGs4iB3Lzg5V7l'

consumer_secret='5TtFzcnZ2iXNPK5XCLYzSVaIUPbxp2NCR8pzU53hpYZ7jiwLtS'

token='346360426-3R934f0ZfOzo7FU4kZ47f2fiZhNN0jU9OEUBgKxF'

token_secret='y1PelClKQ9IaLPqw5ZqWkFyO7qT0ZOBux1vHl2LZp9h33'



t = Twitter(
    auth=OAuth(token, token_secret, consumer_key, consumer_secret))

#t.statuses.home_timeline()

twitter.help()

