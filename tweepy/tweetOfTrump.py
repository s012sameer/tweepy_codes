# get tweets of any user and other descriptions and save in a csv file

import tweepy
import csv

access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

user = "@realdonaldtrump"     #user whose tweets you want to fetch

new_tweets = api.user_timeline(screen_name = user,count=200)
tweets.extend(new_tweets)
last_tweet =tweets[-1].id - 1

while len(new_tweets) > 0:
    print ("getting tweets before %s" % (last_tweet))
    new_tweets = api.user_timeline(screen_name=user, count=200, max_id=last_tweet)
    tweets.extend(new_tweets)
    last_tweet = tweets[-1].id - 1


outTweets = [[tweet.user.name,tweet.user.screen_name,tweet.user.statuses_count,tweet.user.friends_count,
              tweet.user.followers_count,tweet.user.id_str,tweet.user.verified,tweet.user.location,
              tweet.user.description,tweet.created_at,tweet.id_str,tweet.text.encode("utf-8"),
              tweet.lang,tweet.source,tweet.retweeted,tweet.in_reply_to_screen_name,
              tweet.in_reply_to_user_id] for tweet in tweets]

# write the csv
with open('%s.csv'%user, 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['Name','Twitter Handle','Total Tweets','Total followings','Total Followers','User Id',
                     'User Verified','User Location','User Description','Date of tweet','Tweet id','Tweet Text',
                     'Tweet Language','Tweet Source','Tweet Retweet Status','Tweet Reply To Name','Tweet Reply To Id'])
    writer.writerows(outTweets)
pass