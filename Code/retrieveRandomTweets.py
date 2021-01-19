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



def random_tweets(source_file, result_file):

    # Here you should use your own credentials and access tokens for using TwitterAPI.
    api = TwitterAPI('XXXX', 'YYYY', 'ZZZ', 'TTT')
    auth = tweepy.OAuthHandler('XX', 'YY')
    auth.set_access_token('X', 'Y')

    api = tweepy.API(auth, wait_on_rate_limit = True, wait_on_rate_limit_notify = True)
    final_data = []
    i = 0;
    with open(source_file, 'r') as f:
        for line in f.readlines():
            i = i + 1
            print('line = ', i)
            id = ast.literal_eval(line)
            print(id)
            try:
                tweet = api.get_status(id, tweet_mode = "extended")
                print(tweet.id)


                # Clean tweet text
                clean_data = remove_emoji(tweet.full_text)
                clean_data = remove_URL(clean_data)
                clean_data = remove_html(clean_data)

                updated_line = {"id": "%s" % tweet.id_str,
                                "created_at": "%s" % tweet.created_at, "text": "%s" % clean_data}
                final_data.append(updated_line)


            except Exception as e:
                print(e)

        f.close()
    with open(result_file, 'a') as f:
        for item in final_data:
            f.write("%s\n" % item)

    f.close()