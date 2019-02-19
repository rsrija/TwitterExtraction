import tweepy
import csv

####input your credentials here
consumer_key = 'xxxxxx'
consumer_secret = 'xxxxxxxxxxxxxxxxxxx'
access_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
access_token_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxx'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

csvFile = open('testing.csv', 'a')

csvWriter = csv.writer(csvFile)

for tweet in tweepy.Cursor(api.search, q="#blockchain", since="2019-02-14", until="2019-02-15", lang="en", count=1000).items(99999):
    print(tweet.created_at, tweet.text, tweet.retweet_count, tweet.id_str, tweet.user.name, tweet.user.id_str)
    csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.id_str.encode('utf-8'),
                        tweet.user.name.encode('utf-8'), tweet.user.id_str.encode('utf-8')])

