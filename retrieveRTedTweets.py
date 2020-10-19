# This file retrieve full text of some trancated tweets in pattern_X files.
# although the trancated = 'false' in these tweets, some texts are not complete"

from TwitterAPI import TwitterAPI
import tweepy as tweepy
import json
import ast
import re

def main():
    api = TwitterAPI('hh4b8cOLMUC9qOIKPjl9yNr9l', 'guIawTj5ilSkFIZyRj00YtUoLKa7XoOtfCPfdk3thHNPYd8J5c', '1317133968232374273-PjZqMBudPVYRv2ylQ91mEF0ETTtk4u', 'v8tnQVviKyTN9eQDrTrHNMuvNVpkhnhsGx2TbJ3Ly9w1N')
    # ids = "1242043846315380737"

# for item in api.request('users/lookup', {'user_id':ids}):
#         print(item)
    auth = tweepy.OAuthHandler('hh4b8cOLMUC9qOIKPjl9yNr9l', 'guIawTj5ilSkFIZyRj00YtUoLKa7XoOtfCPfdk3thHNPYd8J5c')
    auth.set_access_token('1317133968232374273-PjZqMBudPVYRv2ylQ91mEF0ETTtk4u',
                          'v8tnQVviKyTN9eQDrTrHNMuvNVpkhnhsGx2TbJ3Ly9w1N')
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    final_data = []
    i = 0;
    with open('pattern6.txt', 'r') as f:
        for line in f.readlines():
            i = i + 1
            print('line = ', i)
            data = ast.literal_eval(line)
            # print(data['text'])
            if data['text'].startswith('RT'):
                try:
                    tweet = api.get_status(data['id'], tweet_mode = "extended")
                    updated_line = {"id": "%s" %tweet.retweeted_status.id_str, "created_at": "%s" %tweet.retweeted_status.created_at, "text": "%s" %tweet.retweeted_status.full_text}
                    final_data.append(updated_line)

                except Exception as e:
                    print(e)
            else:
                final_data.append({"id": data['id'], "created_at": data['created_at'], "text": data['text'] })


    f.close()
    # print(final_data,)
    with open('pattern6-noRT.txt', 'a') as f:
        for item in final_data:
            f.write("%s\n" % item)

    f.close()



if __name__ == "__main__":
    main()
