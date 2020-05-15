import tweepy

# Authenticate to Twitter
API_Key = "fJPBBXyfphQrHm2zrLOjAZTQ2"
API_Secret = "GeKdQy3rQpol0QHpCjja6KWGmI526B0NSzTxY4H0uO3oqG03LU"

ACC_Tkn = "1210524582312075264-VSSwldDo9KbiJ3fzO0XDoPyyJkc5Gs"
ACC_Sec = "lS4w8orW5mivFiQDCAALVokzAwkOtkjemzfgPTWKL0eE9"

auth = tweepy.OAuthHandler(API_Key, API_Secret)
auth.set_access_token(ACC_Tkn, ACC_Sec)

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

