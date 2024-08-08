from textblob import TextBlob
import tweepy
import pandas

# Your app's API/consumer key and secret can be found under the Consumer Keys
# section of the Keys and Tokens tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps
consumer_key = "eGI4hh7z1x0szM0QXKqhHkR3e"
consumer_secret = "xiLXxNgfFBSUGYAcKjXli7B5ucSHP1CdGhxIRMOazkNcdtvxU6"


access_token = "1336008035710406657-XhBZdmB1RfehyCebNvraY1Fd2Hd4j4"
access_token_secret = "yg7PGk424mUfotexFUJMdpZxhZd9DUo20YuYhXhktCZWs"

auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

# If the authentication was successful, this should print the
# screen name / username of the account

searchquery = "'UK Riots,'Harrow,UK','Pinner Road' -filter:retweets AND -filter:replies AND -filter:links"
no_of_tweets = 100
tweets= api.search_tweets(searchquery, count=no_of_tweets,lang="en", tweet_mode="extended")
attributes_container = [[tweet.user.name,tweet.created_at, tweet.source,tweet.full_text]for tweet in tweets]

columns = ["User","Data created", "Number of Likes.", "Source of Tweet", "Tweet"]