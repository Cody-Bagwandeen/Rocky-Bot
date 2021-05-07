import tweepy
import time

#personal details
consumer_key = "OELbZ65esoThkaUzFR3HghcP6"
consumer_secret = "C24PhQ0qnhhGSogkgjesuXZ0kZQO7fBgVkNhTOiWXX9w9TflBh"
access_token = "1390737475463786500-qy1ZVgaGeLx7whMWLTMhFwIkyxpI8R"
access_token_secret = "cbg9ceXLdEFBr3n6uuE231WKActxBUKAFbQAw9HRBYeG0"

# authentication of consumer key and secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# authentication of access token and secret
auth.set_access_token(access_token, access_token_secret)
API = tweepy.API(auth)

#                      filename     status
API.update_with_media("rocky.jpg", "loafing")

while True:
    API.update_with_media("rocky.jpg", "loafing")
    print("just tweeted")
    time.sleep(10)
