# Tweets Containing Physical Health Data Disclosure in COVID-19 context

This repository contains the python code to find a set of tweets containing physical health data disclosure in Twitter.
Primary data set for this work is the COVID-19-TweetIDs Dataset (https://github.com/echen102/COVID-19-TweetIDs), containing an ongoing collection of tweets IDs associated with the novel coronavirus COVID-19 (SARS-CoV-2), which commenced on January 28, 2020.
For this research work, only Tweets in English, published between January to July 2020, have been utilized. To comply with Twitter’s Terms of Service, we are only publicly releasing the Tweet IDs of the collected Tweets. The data is released for non-commercial research use.

## Seed words and patterns

Keywords and regular expressions used to find tweets containing health-related data can be found in "keyWordsAndPatterns" folder.
In particular, we were interested in collecting 3 types of disclosure of health-related data about an identifiable individual (the tweeter her/himself or other identifiable individuals including her/him family members). These types are 1) positive medical test result, 2)symptoms of diseases, 3)diseases or other medical conditions.
To find these tweets, we used the following keywords and patterns: 'diseases.txt' contains highrisk diseases for COVID-19, mentioned mainly by the World Health Organization as well as other institutions, while 'symptoms.txt' and 'symptoms.csv' contain reported symptoms of covid-19 on twitter reported in (https://docs.google.com/document/d/1CdhpuNbCV4egYv0TA7hpTqVL3ZfAxyLQipAepDfPzBQ/edit). 
Used regular expressions (containing the mentioned keywords) can also be find in 'pattern.py'.

## Code
This program is written in Python. Scripts for filtering tweets with key words and patterns, cleaning text of the collected tweets from emojis, URLs and html link, replacing the retweets with their original versions, and filling the spreadsheets for tagging data can all be found in the folder 'Code'. Keep in mind that for running some parts of the code you need to obtain your own credential and access token associated with your Twitter developer account(https://developer.twitter.com/en/apply-for-access). 

