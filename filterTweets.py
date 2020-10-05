import re
import json

from tqdm import tqdm
from twarc import Twarc
from pathlib import Path

data_dirs = [ '2020-01','2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08']



final_result = []
def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('.jsonl'):
                analyse(path)



def analyse(id_file):
    tweets_list = []
    seen_Tweets = set()
    print(id_file)
    # keywords = "(positive|negetive|test)"
    pattern_1 = "( uncle| aunt| mother| father| sister| brother| sibling| grandmother| grandfather| aunth| cousin| nephew| children| child| daughter| son)+.*?(test).*?(positive)"
    # pattern_1 = "(I ).*?(test).*?(positive)"
    pattern_2 = "(test).*?(came).*?(back).*?(positive)"
    pattern_3 = "(my).*(symptom)"

    with open(id_file, encoding='utf-8', errors='ignore') as f:
        for line in f.readlines():
            try:
                data = json.loads(line)
                if data["lang"] == "en" and data["full_text"] not in seen_Tweets:
                    res = re.findall(pattern_1, data['full_text'])
                    if len(res) != 0:
                        # tweets_list.append({'id': data['id'], 'text': data['full_text']})
                        write_to_file([{'id': data['id'], 'text': data['full_text']}])
                        seen_Tweets.add(data["full_text"])
            except ValueError as e:
                pass



def write_to_file(myList):

    with open('pattern1.txt', 'a') as f:
        for item in myList:
            f.write("%s\n" % item)


if __name__ == "__main__":
    main()