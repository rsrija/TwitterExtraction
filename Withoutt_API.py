import tweepy
import csv
import math
####input your credentials here
consumer_key = '24zbsmc6ldwhjZOvMx5uBRmDP'
consumer_secret = 'ai6ZiZ6doCnaND91CDateDHCrTED7sUUigj2sg0bdKw0kUp7tj'
access_token = '933490253570064384-wV6q851kU9RBUC9JF87L5tR5iGj1zkV'
access_token_secret = 'CJ43YjTVJJrS0wkUPsOiO0pl4wezsP98OVl7eXxNoQjFx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)
csvFile = open('testing2.csv', 'a')

csvWriter = csv.writer(csvFile)
user="Ripple"
results = api.user_timeline(screen_name = user, count = 50)

for tweet in results:
    if tweet.retweet_count > 300:
        print(tweet.created_at, tweet.text, tweet.retweet_count, tweet.id_str, tweet.user.name, tweet.user.id_str)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.id_str.encode('utf-8'),
                        tweet.user.name.encode('utf-8'), tweet.user.id_str.encode('utf-8'),math.log(tweet.retweet_count,10)])

api.update_status(status ="Hello Everyone !") 