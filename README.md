# Hackathon
Hackathon organized by McGill AI Society

## Inspiration
Polls shine a light onto the political landscape of a country and have the power to influence voter behavior [1]. 

The previous US election has demonstrated shortcomings in polling strategies. One commonly cited explanation for the failure of pollings in 2016 is nonresponse bias [2]. Not all groups respond to pollings in comparable numbers and therefore equal representation might not be achieved.

Our goal was to explore Twitter as a remedy to nonresponse bias and an additional tool for exploring population sentiment.  

## What it does
We generated a model that predicts the sentiment expressed in tweets towards either of the political candidates. 

Tweets can subsequently be queried by geolocation and labeled through our model. The resulting data can then be aggregated by location and used to assess political sentiment.

## How we built it
We collected our own data by using a twitter scraper and querying several hashtags associated with positive sentiments towards either political candidate (#conservative vs. #BidenHarris2020). 

We then parsed tweet texts and labeled the data by hand to not entirely rely on the hashtags. Tweets were given one out of three labels, two for positive sentiments towards either one of the candidates and a third for neutral sentiment.

To map the tweets onto a feature space we employed a bag-of-words model using NLTK. Finally, we used our generated features to create a Naive Bayes classifier that achieved an accuracy of over 76% on the validation set.
  
## Challenges we ran into
The data we obtained from the scraper was messy and each tweet came in a separate text file. We had to find a way to merge all files together and extract only the tweet text.

After that, we encountered a fair amount of sarcasm in our scraped tweets, which is impossible to detect through a simple bag-of-words model. This is difficult even with sophisticated embeddings.

## Accomplishments that we're proud of
We are proud of having compiled our own training data and of the 76% validation accuracy that our model achieved.

## What we learned
The importance of teamwork under time constrains.

## What's next for Lighthouse
The next step would be to obtain more data, preferably through the Twitter API, and to use a more sophisticated transformer model such as BERT.

Lastly, we would query Twitter based on geolocation and use our model to aggregate political sentiments with a focus on swing-states.

## References
[1] https://www.gsb.stanford.edu/insights/how-polls-influence-behavior  
[2] https://www.pewresearch.org/fact-tank/2016/11/09/why-2016-election-polls-missed-their-mark/
