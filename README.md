# Using Machine Learning based on Tweets to understand the Usage of parks in Stockholm.
This project was conducted as a Bachelor thesis were I explored the potential of Natural langugage Processing(NLP) techniques based on Twitter data to understand the Usage of parks in Stockholm. NLP is a field within Machine learning with the ability of a computer to read, understand and dervie meaning from the human language through text or speech.
<br/>
For full description: [Degree report](http://www.diva-portal.se/smash/get/diva2:1453846/FULLTEXT01.pdf)
## Introduction
This project Uses Natural Langugage Processing techniques based on Tweets from Twitter in order to understand the usage of parks in Stockholm. Data from Twitter were first obtained through Twitters open API. Data from three parks in Stockholm were collected between the periods 2015-2019. Following three parks were seleted:
1. **Hagaparken**.
2. **Skogskyrkogården**.
3. **Rålambshovsparken**.<br/>

Three analysis were then performed, **Temporal**, **Sentiment** and **Topic Modeling** analysis. Following questions were then investigated:<br/>

* **Temporal analysis**: *How does the distribution of parks vary over time? Yearly, monthly, weekly, hourly and seasonally*.
* **Sentiment analysis**: *What sentiment, positive ,negative or neutral are associated with Tweets from parks*.
* **Topic Modeling analysis**: *What are the activities people engage in while visiting parks*.

## Built with
Throughout the project **Python** was used. **Pandas DataFrame** was used for data manipulation, preprocessing and analysis. The Sentiment analysis classification was performed using the **VADER** lexicon and corresponding data preprocessing used pythons **nltk** library. The Topic modeling algorithm used was the **LDA-model**. All grahps was created using **Seaborn**.

* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [VADER](https://github.com/cjhutto/vaderSentiment)
* [nltk](https://www.nltk.org/)
* [LDA explanation](https://www.analyticsvidhya.com/blog/2016/08/beginners-guide-to-topic-modeling-in-python/)
* [Seaborn](https://seaborn.pydata.org/)

## Getting Started
### 1. Installation
Below packages are used in this project and can be installed in the command terminal as follows:
* **Pandas** <br/>
Used for data analysis and preprocessing.
> pip install pandas 

* **Seaborn** <br/>
Used for plotting.
> pip install seaborn

* **VADER** <br/>
Used for performing sentiment analysis.
> pip install vaderSentiment

* **nltk** <br/>
Used for stemming and cleaning for stopwords.
> pip install nltk

* **gensim** <br/>
Used for Topic modeling.
> pip install gensim <br/>

### 2. Twitter API key
In order to obtain data from Twitters API, authentication-keys is needed which requires a developer account. 
1. Create a free twitter developer account. [Creating Free account and Getting started Step by Step](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)
2. Generate Authentication keys.
3. Add the authentication keys(created in step 2) into "Tokens_Keys.py" file(in the "Query_and_Authentication" folder).

## Twitter Data
Data from Twitter were obtained through Twitters API. **The premium search API** was used which allows users to make 30 request every minute with a maximum of of 100 tweets being obtained for each request and with a limit of 50 request each minute. 
* [Premium search query](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/premium-search)

Twitter data for each park was obtained through a conditional statement including Keyword, hastag(#) and bounding box as follows:
<br/>

**Obtained Twitter-data for each park** = *Keyword* **OR** *Hashtag(#)* **OR** *Bounding box*.
<br/>

The response of the above request is a **JSON-object** containing a large amount of metadata for which the metadta ***"Created_at"***(timestamp) and ***"text"***(Tweet) were extracted and cleaned for duplicates before respective analysis was performed. 

## Temporal analysis
For this analysis the metadata ***"Created_at"*** was extracted and loaded into a Pandas DataFrame and four graphs were created using Seaborn.<br/>
1. **Montly** distribution of park-Tweets.
2. **Weekday** distribution of park-Tweets.
3. **Date of the year** distribution of park-Tweets.
4. **Hourly** distribution of park-Tweets.

## Sentiment analysis
For this analysis the metadata ***"Created_at"*** and ***"text"*** was loaded into a Pandas DataFrame. The text-data was first cleaned for all characters that doesnt influence the sentiment then stemmed and furthermore cleaned for stopwords using **nltk**. Then the **VADER** lexicon was  used to automatically classify each tweet according to its semantic orientation. The compound metric was used for the classification of the sentiment score, each tweet was given a score between **-1**(most extreme negative) and **+1**(most extreme positive).<br/>

Each tweet was then classified into either **positive**, **negative** or **neutral** based on the sentiment score given by VADER. The classification into the respective categories was based using the typical threshold for classifying the polarity in text as follows. 
* **Positive Sentiment:** Compound score > 0.05
* **Negative Sentiment:** Compound score < -0.05
* **Neutral Sentiment:** -0.05 < Compound score < 0.05

Four plots were then created for each park as follows:


1. **Seasonal** distribution of Sentiment.
2. **Monthly** distribution of Sentiment Score.
3. **Weekday** distribution of Sentiment Score.
4. **Hourly** distribution of Sentiment. 


## Topic Modeling
For this analysis the metadata ***"Created_at"*** and ***"text"*** was loaded into a Pandas DataFrame. All characters that wasnt a alphabetic letter was then removed. Only **nouns**, **adjective** and **verbs** was used for analysis. After this step the DataFrame could be transformed into a **Document Term Matrix** which is the required input in Topic modeling and then by using the Python module Gensim the **LDA algorithm** could be implemented. 

The LDA model was first run for the pre-determined topics of ***two***, ***three*** and ***four***. The pre-determined number of topics used as input to the LDA model was determined based on the output from the respective of the above number of topics. Below is the number of topics selected for each park:

* **Hagaparken**: 4 topics.
* **Skogskyrkogården**: 3 topics.
* **Rålambshovsparken**: 3 topics.

Two plots were then created for each park. 

1. **Word-cloud plot:** Visualizing the twenty most common words expressed.
2. **Bar plot:** Visualizing the distribution of tweets talking about one of the ***k*** topics.








