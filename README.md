# MAIS Hacks 2020
Hackathon organized by the McGill AI Society

## Installation
**Packages**: numpy, pandas, scikit-learn, nltk, tokenize, re, os   
**Twitter Scraper:** https://github.com/jonbakerfish/TweetScraper

## Inspiration
Polls shine a light onto the political landscape of a country and have the power to influence voter behavior [1]. 

The previous US election has demonstrated shortcomings in polling strategies. One commonly cited explanation for the failure of pollings in 2016 is nonresponse bias [2]. Not all groups respond to pollings in comparable numbers and therefore equal representation might not be achieved.

Our goal was to explore Twitter as a remedy to nonresponse bias and an additional tool for probing population sentiment. Lighthouse can be used to monitor political support on a large sample of the population.  

## What it does
We generated a model that predicts the sentiment expressed in tweets towards either of the political candidates. 

Tweets can subsequently be queried by geolocation and labeled through our model. The resulting data can then be aggregated by location and used to assess political sentiment. The pipeline can be also used to monitor recent tweets on twitter and used for further analyses. Similar pipelines can also be implemented to monitor posts on other social media such as Facebook, Reddit or other specific forum to monitor the sentiments of the users.

## How we built it
We collected our own data by using a twitter scraper and querying several hashtags associated with positive sentiments towards either political candidate (#conservative vs. #BidenHarris2020). 

We then parsed tweet texts and labelled the data by hand to not entirely rely on the hashtags. Tweets were given one out of three labels, two for positive sentiments towards either one of the candidates and a third for neutral sentiment.

We used the NLTK package to build our bag-of-words in order to map the tweets onto a feature space. Finally, we fed our generated features into different ML models (SVM, LR, NB). The best model is our Naive Bayes classifier, it achieved an accuracy of over 76% on the validation set. At the beginning of the hackathon, we planed to use more advance DL models such as LSTM, Bert, or Xlnet, unfortunately, due to the tweet scraper failure, we didn't have time to train a more sophisticated model, but our result shows that useful sentiments towards an event (such as election2020) can be learned from social media.
  
## Challenges we ran into
The data we obtained from the scraper was messy and each tweet came in a separate text file. We had to find a way to merge all files together and extract only the tweet text.

Cleaning text data is also a challenge for us, since in the team, no member has the domain knowledge of NLP. This project became a good opportunity for all us to get our hands dirty. Especially, we encountered a fair amount of sarcasm in our scraped tweets, which is very difficult for ML models to learn. This is difficult even with sophisticated embeddings.

## Accomplishments that we're proud of
We are proud of having compiled our own training data and of the 76% validation accuracy that our model achieved.

## What we learned
The importance of teamwork under time constrains.

## What's next for Lighthouse
The next step would be to obtain more data, preferably through the Twitter API, and to use a more sophisticated transformer model such as BERT. 

We would then query Twitter based on geolocation and use our model to aggregate political sentiments with a focus on swing-states.

Lastly, similar results can be obtained by tracking other social media to get a more accurate snapshot political support in the population.

## References
[1] https://www.gsb.stanford.edu/insights/how-polls-influence-behavior  
[2] https://www.pewresearch.org/fact-tank/2016/11/09/why-2016-election-polls-missed-their-mark/  

Link to Devpost: https://devpost.com/software/lighthouse-u9wadz
