import tweepy

# Authenticate to Twitter
API_Key = "fJPBBXyfphQrHm2zrLOjAZTQ2"
API_Secret = "GeKdQy3rQpol0QHpCjja6KWGmI526B0NSzTxY4H0uO3oqG03LU"

ACC_Tkn = "1210524582312075264-VSSwldDo9KbiJ3fzO0XDoPyyJkc5Gs"
ACC_Sec = "lS4w8orW5mivFiQDCAALVokzAwkOtkjemzfgPTWKL0eE9"



auth = tweepy.OAuthHandler(API_Key, API_Secret)
auth.set_access_token(ACC_Tkn, ACC_Sec)
api = tweepy.API(auth)

print("-----------")
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

print("-----------")
user = api.get_user("MikezGarcia")
print("User details:")
print(user.name)
print(user.description)
print(user.location)

#print("-----------")
#timeline = api.home_timeline()
#for tweet in timeline:
#    print(f"{tweet.user} said {tweet.text}")


print("-----------")
print(user.screen_name)
print(user.followers_count)
for friend in user.friends():
   print(friend.screen_name)

print("------ Searches ------")
for tweet in api.search(q="BTC", lang="en", rpp=10):
    print(f"{tweet.user.name}:{tweet.text}")

print("------ Trends ------")
trends_result = api.trends_place(1)
for trend in trends_result[0]["trends"]:
    print(trend["name"])

print("------ Streaming ------")
class MyStreamListener(tweepy.StreamListener):
    def __init__(self, api):
        self.api = api
        self.me = api.me()

    def on_status(self, tweet):
        print(f"{tweet.user.name}:{tweet.text}")

    def on_error(self, status):
        print("Error detected")

tweets_listener = MyStreamListener(api)
stream = tweepy.Stream(api.auth, tweets_listener)
stream.filter(track=["BTC", "BTC Split"], languages=["en"])

