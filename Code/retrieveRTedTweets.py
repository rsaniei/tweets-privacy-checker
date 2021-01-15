# This file retrieves the original tweets when they are in form of RT (re-tweeted)
# in a resulted file (source_file), using tweepy package and Twitter API,
# and save a new version of source_file, removing RT tweets and replacing the original ones.

from TwitterAPI import TwitterAPI
import tweepy as tweepy
import json
import ast
import re
from cleanTweets import *

# Here, for example source_file = 'pattern1.txt'
# Here, for example source_file = 'pattern1-noRT.txt'

def retrieve_rt(source_file, source_file_noRT):

    # Here you should use your own credentials and access tokens for using TwitterAPI.
    api = TwitterAPI('XXXX', 'YYYY', 'ZZZ', 'TTT')
    auth = tweepy.OAuthHandler('XX', 'YY')
    auth.set_access_token('X','Y')

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    final_data = []
    i = 0;
    with open(source_file, 'r') as f:
        for line in f.readlines():
            i = i + 1
            print('line = ', i)
            data = ast.literal_eval(line)
            # print(data['text'])
            if data['text'].startswith('RT'):
                try:
                    tweet = api.get_status(data['id'], tweet_mode = "extended")

                    # Clean tweet text
                    clean_data = remove_emoji(tweet.retweeted_status.full_text)
                    clean_data = remove_URL(tweet.retweeted_status.full_text)
                    clean_data = remove_html(tweet.retweeted_status.full_text)

                    updated_line = {"id": "%s" %tweet.retweeted_status.id_str, "created_at": "%s" %tweet.retweeted_status.created_at, "text": "%s" %clean_data}
                    final_data.append(updated_line)

                except Exception as e:
                    print(e)
            else:
                final_data.append({"id": data['id'], "created_at": data['created_at'], "text": data['text'] })


    f.close()

    with open(source_file_noRT, 'a') as f:
        for item in final_data:
            f.write("%s\n" % item)

    f.close()