import re
import json

from tqdm import tqdm
from twarc import Twarc
from pathlib import Path
from filterTweets import find_pattern

data_dirs = ['2020-01','2020-02', '2020-03', '2020-04', '2020-05', '2020-06', '2020-07', '2020-08']
seen_tweets = set()


def main():
    for data_dir in data_dirs:
        for path in Path(data_dir).iterdir():
            if path.name.endswith('.jsonl'):
                find_pattern(path, seen_tweets)


if __name__ == "__main__":
    main()