import tweepy
import csv

access_token = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
access_token_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_key = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
consumer_secret = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

tweets = []

user = "@abcde"     #your screen/user name

new_tweets = api.user_timeline(screen_name =user,count=200)
tweets.extend(new_tweets)
last_tweet =tweets[-1].id - 1


while len(new_tweets) > 0:
    print ("getting tweets...please wait...")
    new_tweets = api.user_timeline(screen_name=user, count=200, max_id=last_tweet)
    tweets.extend(new_tweets)
    last_tweet = tweets[-1].id - 1

print("Total tweets : "+str(len(tweets)))

if(input("Confirm to delete (Y/n) :")=='Y'):
	for tweet in tweets:
		api.destroy_status(tweet.id_str)
	print("Deleted")
else:
	print("Cancelled!!")