# Using NLP based on Twitter tweets in order to understand the Usage of parks in Stockholm.
This project was conducted as a Bachelor degree project were I explored the potential of Twitter data and NLP techniques to understand the Usage of parks in Stockholm.<br/>
For full despricption: [Degree report](http://www.diva-portal.se/smash/get/diva2:1453846/FULLTEXT01.pdf)
## Introduction
This project Uses Natural Langugage Processing techniques based on Tweets from Twitter in order to understand the usage of parks in Stockholm.
Data from Twitter were first obtained through Twitters open API. Data from three parks in Stockholm were collected between the periods 2015-2019.
Three analysis were then performed, Temporal, Sentiment and Topic Modeling analysis. Each analysis aimed to answer the following questions:

* **Temporal analysis**: How does the distribution of parks vary over time? Yearly,monthly,weekly,hourly, and seasonally.
* **Sentiment analysis**: What sentiment,positive,negative or neutral are associated with Tweets from parks.
* **Topic Modeling analysis**: What are the activities people engage in while visiting parks.

## Built with
Python was used during all steps in this project. Pandas DataFrame was used for performing the respective analysis including data preprocessing. All plots was created
through Seaborn, a python data visualization library. Sentiment analysis was performed using the VADER lexicon. 
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Seaborn](https://seaborn.pydata.org/)
* [VADER] (https://github.com/cjhutto/vaderSentiment)

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
Used for data preprocessing.
> pip install nltk

* **gensim** <br/>
Used for Topic modeling.
> pip install gensim <br/>

### 2. Twitter API key
In order to obtain data from Twitter autentification keys is needed which requires a developer account. 
1. Create a free twitter developer account. [Creating Free account and Getting started Step by Step](https://developer.twitter.com/en/docs/twitter-api/getting-started/guide)
2. Generate Autentification keys.

## Twitter Data
Data from Twitter were obtained through Twitters API.The premium search API was used which allows users to make 30 request every minute with a maximum of of 100 tweets being obtained for each request and with a limit of 50 request each minute. 
* [Premium search query](https://developer.twitter.com/en/docs/twitter-api/v1/tweets/search/api-reference/premium-search)

Twitter data for ech park was obtained through a conditional statement including Keyword,hastag(#) and bounding box as follows:<br/>
**Obtained tweet for each park** = *Keyword* **OR** *Hashtag(#)* **OR** *Bounding box*.<br/>
The response of the above Query is a JSON-object containing metadata for which the metadta *"Created_at"*(timestamp) and *"text"*(Tweet) were extracted and cleaned for duplicates. 

## Temporal analysis

## Sentiment analysis

## Topic Modeling


