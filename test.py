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

raw_text = []
for dat in data:
    text = re.search("full_text\": \".*", dat)
    try:
        t = text.group()[: 400]
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
    clean = re.search('"(.*?)"', trimmed)
    try:
        clean_text.append(clean.group())
    except:
        print('='*50)
        print('Could not match:')
        print('='*50)
        
df = pd.DataFrame({'tweets': clean_text})

low_character_count = df.tweets.apply(lambda x: len(x))
low_character_count.hist(bins=range(0, 380, 10))

# Cut off records with less than 30 characters
df = df[low_character_count > 30]
df.to_csv("pro_trump2.csv")