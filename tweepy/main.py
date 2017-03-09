import tweetsByHashTag,tweetsOfUser,tweetsToUser
def get_tweets():
    print("== WELCOME ==")

    while(True):
        print("Select action: ")
        print("1. Get tweets by an USER\n2. Get tweets to an USER\n3. Get tweets with a HASHTAG\n4. Exit")
        try:
            c = int(input("Your choice: "))
        except ValueError:
            print ("Wrong action. Please try again\n")
            continue
        if c == 4:
            break
        elif c == 1:
            tweetsOfUser.tweets_by_user()
        elif c== 2:
            tweetsToUser.tweets_to_user()
        elif c == 3:
            tweetsByHashTag.tweets_by_hashtag()

if __name__ == "__main__":
    get_tweets()