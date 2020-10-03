import pandas as pd 
import twitterscraper
from twitter_scraper import get_tweets

# from twitterscraper import query_tweets

# if __name__ == '__main__':
#     list_of_tweets = query_tweets("Trump OR Clinton", 10)

#     #print the retrieved tweets to the screen:
#     for tweet in query_tweets("Trump", 10):
#         print(tweet)

#     #Or save the retrieved tweets to file:
#     file = open("output.txt","w")
#     for tweet in query_tweets("Trump OR Clinton", 10):
#         file.write(str(tweet.text.encode('utf-8')))
#     file.close()



# List of hashtags that we're interested in
keywords = ['#MAGA', '#Trump2020', '#antitrump']

for tweet in get_tweets('#twitter', pages=1):
    print(tweet['text'])
    
tweets = get_tweets("#MAGA", 5)
