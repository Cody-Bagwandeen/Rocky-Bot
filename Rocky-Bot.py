import tweepy
import time

#personal details
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

#                      filename     status
#API.update_with_media("pictures/" + "rocky.jpg", "loafing")

while True:
    API.update_with_media("pictures" + "/rocky.jpg", "loafing")
    print("just tweeted")
    time.sleep(3)
