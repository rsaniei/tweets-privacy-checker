import json
import re
import random

# select 'rand_num' number of tweetId from the file in 'path' and write them in result_file'
def select_random(path, result_file, rand_num):

    with open(path, "rb") as source:
        lines = [line for line in source]

    random_choice = random.sample(lines, rand_num)


    with open(result_file, 'a') as f:
        for item in lines:
            f.write("%s\n" % item)

