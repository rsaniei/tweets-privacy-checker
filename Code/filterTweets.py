
import re
import json
from cleanTweets import *
from patterns import *


# This function gets the id of a jsonl file, which has a complete tweet (id, fulltext, etc.) in each line.
# Then, one by one, it checks if a certain pattern can be found in the full_text of a tweet
# It also ignores the replicate tweets.

def find_pattern(id_file, seen_tweets, pattern_num ,result_file):

    if  pattern_num == 0:
        pattern = pattern_0
    elif  pattern_num == 1:
        pattern = pattern_1
    elif pattern_num == 2:
        pattern = pattern_2
    elif pattern_num == 3:
        pattern = pattern_3
    elif pattern_num == 4:
        pattern = pattern_4
    elif pattern_num == 5:
        pattern = pattern_5
    elif pattern_num == 6:
        pattern = pattern_6
    elif pattern_num == 7:
        pattern = pattern_7

    tweets_list = []
    print(id_file)

    with open(id_file, encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            try:
                data = json.loads(line)

                if data["lang"] == "en" and data["full_text"] not in seen_tweets:

                    original_data = data['full_text']
                    data['full_text'] = remove_emoji(data['full_text'])
                    data['full_text'] = remove_URL(data['full_text'])
                    data['full_text'] = remove_html(data['full_text'])
                    # data['full_text'] = remove_punct(data['full_text'])

                    res = pattern.findall(data['full_text'])

                    if len(res) != 0:
                        write_to_file(result_file, [{'id': data['id'], 'created_at':data['created_at'],'text': data['full_text']}])
                        seen_tweets.add(original_data)
            except ValueError as e:
                pass



def write_to_file(result_file, myList):
    with open(result_file, 'a') as f:
        for item in myList:
            f.write("%s\n" % item)
