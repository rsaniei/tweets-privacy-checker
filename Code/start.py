import re
import json

from tqdm import tqdm
from twarc import Twarc
from pathlib import Path
from filterTweets import find_pattern
from filterTweetsforSymptoms import find_symptoms
from fillSpreadsheets import fill_spreadsheet


def main():

    # Fill with your own values

    spreadsheet_id = '1Jvw5gEe8Zt5hszvdlMcHcL3VNFJN-lt9dWZ_BV3O5B0'
    source_file = 'pattern7.txt'
    sheet_title = 'test1!A1:E'
    fill_spreadsheet(spreadsheet_id, source_file, sheet_title)


if __name__ == "__main__":
    main()