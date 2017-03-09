import tweepy
import csv

access_token = "442755126-QUgyMQjAPllOBGqqy3hTgbeebs6PxJYBI6S2kKUf"
access_token_secret = "sAAgCvku936UnBOkJkISBzZ6qoz7u7DLhm3TdqL7HKBQs"
consumer_key = "6sgX2e6bRdzgK0sSS0jZc1Jgc"
consumer_secret = "qPopztsGzJAxqaqOXWYZ2r3TJOicYilFqFTnB6gXYBmiD1vXCR"

def tweets_by_user():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = []

    user = input("Enter username : ")  #username whose tweets are needed

    new_tweets = api.user_timeline(screen_name = user,count=200)
    tweets.extend(new_tweets)
    last_tweet =tweets[-1].id - 1


    while len(new_tweets) > 0:
        print ("getting tweets before %s" % (last_tweet))
        new_tweets = api.user_timeline(screen_name=user,count=200,max_id=last_tweet)

        tweets.extend(new_tweets)
        last_tweet = tweets[-1].id - 1

        print("...%s tweets downloaded so far" % (len(tweets)))

    outTweets = [[tweet.user.name,tweet.user.screen_name,tweet.user.statuses_count,tweet.user.friends_count,
                  tweet.user.followers_count,tweet.user.id_str,tweet.user.verified,tweet.user.location,
                  tweet.user.description,tweet.created_at,tweet.id_str,tweet.text,
                  tweet.lang,tweet.source,tweet.retweeted,tweet.in_reply_to_screen_name,
                  tweet.in_reply_to_user_id] for tweet in tweets]

    # write the csv

    with open(user+'.csv', 'w',newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name','Twitter Handle','Total Tweets','Total followings','Total Followers','User Id',
                         'User Verified','User Location','User Description','Date of tweet','Tweet id','Tweet Text',
                         'Tweet Language','Tweet Source','Tweet Retweet Status','Tweet Reply To Name','Tweet Reply To Id'])
        writer.writerows(outTweets)
    pass

if __name__ == " __main__ ":
    tweets_by_user()