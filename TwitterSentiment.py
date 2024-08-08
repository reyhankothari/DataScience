from textblob import TextBlob
import tweepy
import pandas
from dotenv import load_dotenv
import os

load_dotenv()



# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")


access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)


print(api.verify_credentials().screen_name)

# If the authentication was successful, this should print the
# screen name / username of the account

# searchquery = "'UK Riots,'Harrow,UK','Pinner Road' -filter:retweets AND -filter:replies AND -filter:links"
# no_of_tweets = 100
# tweets= api.search_tweets(searchquery, count=no_of_tweets,lang="en", tweet_mode="extended")
# attributes_container = [[tweet.user.name,tweet.created_at, tweet.source,tweet.full_text]for tweet in tweets]

# columns = ["User","Data created", "Number of Likes.", "Source of Tweet", "Tweet"]