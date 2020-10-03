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

hashtags = "#maga #trump #donaldtrump #conservative #republican #makeamericagreatagain\
        #keepamericagreat #america #trumptrain #draintheswamp #americafirst #walkaway\
        #thegreatawakening #buildthewall #fakenews #trumpsupporters #gop"

# List of hashtags that we're interested in
keywords = ['#MAGA', '#Trump2020', '#antitrump']

for tweet in get_tweets('#twitter', pages=1):
    print(tweet['text'])
    
tweets = get_tweets("#MAGA", 5)

def dict_from_file(f):
    def line_splitter(line):
        items = line.strip().split()
        return items[0], items[1:]
    # To use filenames, change 'f' above to filename and
    # use this line:
    # with open(filename) as f:
    return {k:v
            for line in f
            for k, v in (line_splitter(line),)}

import os
import json
import re
data = []
directory = '/home/jahnic/Git/Hackathon/TweetScraper/Data/tweet'
for filename in os.listdir(directory):
    tweet_file = directory + "/" + filename
    with open(tweet_file, 'r') as file:
        tweet_data = file.read()
     
    data.append(tweet_data)

# raw_text = []
# for dat in data:
#     text = re.search("full_text\": \"[0-9a-zA-Z,.’'@#\s\*]+", dat)
#     try:
#         raw_text.append(text.group())
#     except:
#         print('='*50)
#         print('Could not match:', data[140:200])
#         print('='*50)
# full_text

raw_text = []
for dat in data:
    text = re.search("full_text\": \".*", dat)
    try:
        t = text.group()[: 300]
        raw_text.append(t)
    except:
        print('='*50)
        print('Could not match:')
        print('='*50)
raw_text

clean_text = []
for txt in raw_text:
    # trim 'full_text": from txt 
    trimmed = txt[12:]
    clean = re.search('.*@*\"', trimmed)
    try:
        clean_text.append(clean.group())
    except:
        print('='*50)
        print('Could not match:')
        print('='*50)
        
clean_text[8]
raw_text[8][13:]