import tweepy
import csv

access_token = ""
access_token_secret = ""
consumer_key = ""
consumer_secret = ""

def tweets_by_hashtag():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    tweets = []

    searchQuery = input("Enter the #HashTag to search tweets : ")  # this is what we're searching for
    maxTweets = int(input("Number of tweets (min - 100) : ")) # No of tweets needed
    tweetsPerQry = 100  # this is the max the API permits
    fName = searchQuery +".csv" # We'll store the tweets in a text file.


    # If results from a specific ID onwards are reqd, set since_id to that ID.
    # else default to no lower limit, go as far back as API allows
    sinceId = None

    # If results only below a specific ID are, set max_id to that ID.
    # else default to no upper limit, start from the most recent tweet matching the search query.
    max_id = -1

    tweetCount = 0
    print("Downloading max {0} tweets".format(maxTweets))
    with open(fName, 'w',newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ['Name', 'Twitter Handle', 'Total Tweets', 'Total followings', 'Total Followers', 'User Id',
             'User Verified', 'User Location', 'User Description', 'Date of tweet', 'Tweet id', 'Tweet Text',
             'Tweet Language', 'Tweet Source', 'Tweet Retweet Status', 'Tweet Reply To Name',
             'Tweet Reply To Id'
             ])

        while tweetCount < maxTweets:
            try:
                if (max_id <= 0):
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry,lang="en")
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                since_id=sinceId,lang="en")
                else:
                    if (not sinceId):
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1),lang="en")
                    else:
                        new_tweets = api.search(q=searchQuery, count=tweetsPerQry,
                                                max_id=str(max_id - 1),
                                                since_id=sinceId,lang="en")
                if not new_tweets:
                    print("No more tweets found")
                    break
                for tweet in new_tweets:
                    outTweets = [tweet.user.name.encode('utf-8'), tweet.user.screen_name.encode('utf-8'),
                                 tweet.user.statuses_count, tweet.user.friends_count,
                         tweet.user.followers_count, tweet.user.id_str.encode('utf-8'), tweet.user.verified,
                         tweet.user.location.encode('utf-8'),
                         tweet.user.description.encode('utf-8'), tweet.created_at, tweet.id_str.encode('utf-8'),
                         tweet.text.encode('utf-8'),
                         tweet.lang, tweet.source, tweet.retweeted, tweet.in_reply_to_screen_name,
                         tweet.in_reply_to_user_id]

                    writer.writerow(outTweets)
                tweetCount += len(new_tweets)
                print("Downloaded {0} tweets".format(tweetCount))
                max_id = new_tweets[-1].id
            except tweepy.TweepError as e:
                # Just exit if any error
                print("some error : " + str(e))
                break

if __name__ == " __main__ ":
    tweets_by_hashtag()
