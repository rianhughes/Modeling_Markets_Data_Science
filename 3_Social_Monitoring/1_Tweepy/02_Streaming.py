import tweepy
import sys

# Authenticate to Twitter
API_Key = "fJPBBXyfphQrHm2zrLOjAZTQ2"
API_Secret = "GeKdQy3rQpol0QHpCjja6KWGmI526B0NSzTxY4H0uO3oqG03LU"

ACC_Tkn = "1210524582312075264-VSSwldDo9KbiJ3fzO0XDoPyyJkc5Gs"
ACC_Sec = "lS4w8orW5mivFiQDCAALVokzAwkOtkjemzfgPTWKL0eE9"



auth = tweepy.OAuthHandler(API_Key, API_Secret)
auth.set_access_token(ACC_Tkn, ACC_Sec)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

print("------ Streaming ------")
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")
        print(status)
        return False # Disconnects
        #sys.exit()

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
print(stream.filter(track=["BTC", "BTC Split"], languages=["en"]))

