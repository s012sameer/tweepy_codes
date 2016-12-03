import tweepy
import csv

access_token = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_token_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

user = "realdonaldtrump"  #username whose tweets are needed

new_tweets = api.user_timeline(screen_name = user,since='2016-01-01 00:00:00',until='2016-11-01 00:00:00',count=200)
tweets.extend(new_tweets)
last_tweet =tweets[-1].id - 1


while len(new_tweets) > 0:
    print ("getting tweets before %s" % (tweets[-1].created_at))
    new_tweets = api.user_timeline(screen_name=user, since='2016-01-01 00:00:00',until='2016-11-01 00:00:00',count=200, max_id=last_tweet,
                                   wait_on_rate_limit=True)

    tweets.extend(new_tweets)
    last_tweet = new_tweets[-1].id - 1


outTweets = [[tweet.user.name,tweet.user.screen_name,tweet.user.statuses_count,tweet.user.friends_count,
              tweet.user.followers_count,tweet.user.id_str,tweet.user.verified,tweet.user.location,
              tweet.user.description,tweet.created_at,tweet.id_str,tweet.text.encode("utf-8"),
              tweet.lang,tweet.source,tweet.retweeted,tweet.in_reply_to_screen_name,
              tweet.in_reply_to_user_id] for tweet in tweets]

# write the csv

with open('csv/realdonaldtrump.csv', 'w',newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Twitter Handle','Total Tweets','Total followings','Total Followers','User Id',
                     'User Verified','User Location','User Description','Date of tweet','Tweet id','Tweet Text',
                     'Tweet Language','Tweet Source','Tweet Retweet Status','Tweet Reply To Name','Tweet Reply To Id'])
    writer.writerows(outTweets)
pass
