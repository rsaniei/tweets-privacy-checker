
# This function get the id of a .jsonl files, which has a complete tweet (id, fulltext, etc.) in each line
# and a csv file contains in each line a reported symptom of the covid-19 in twitter.
# Then, one by one, it checks if a certain symptom can be found in the full_text of a tweet.
# Replicate tweets are ignored.
# Finally, found tweets are saved in the result_file file.
import re
import json
from cleanTweets import *

# Here, csv_file = 'symptoms.csv'
# Here,result_file = 'pattern-symptoms.txt'

def find_symptoms(id_file, seen_tweets, csv_file, result_file):

    tweets_list = []
    print(id_file)

    with open(csv_file) as f:
        content = f.readlines()
    # you may also want to remove whitespace characters like `\n` at the end of each line
    content = [x.strip() for x in content]

    pattern = re.compile(r"(?=("+' | '.join(content)+r"))")
    print(pattern)


    with open(id_file, encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
             try:
                 data = json.loads(line)

                 if data["lang"] == "en" and data["full_text"] not in seen_tweets:

                     original_data = data['full_text']
                     data['full_text'] = remove_emoji(data['full_text'])

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
