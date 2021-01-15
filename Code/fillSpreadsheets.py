from __future__ import print_function
import pickle
import os.path
import re
import ast
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# This script fills a sheet(range_name) of google spreadsheet document(spreadsheet_id)
# with objects of tweets stored in a file (source_name).


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def fill_spreadsheet(spreadsheet_id, source_name, range_name):

    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
            print('no credential found!')
        else:
            # save your own credentials in your path
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    try:
        service = build('sheets', 'v4', credentials=creds)

        # Call the Sheets API
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=spreadsheet_id,
                                    range = range_name).execute()
        # return service
    except Exception as e:
        print(e)


    i = 0
    with open(source_name, 'r') as f:
        mydata = []
        for line in f:
            print(i)
            i = i +1
            data = ast.literal_eval(line)
            if (data['text'].startswith('RT') == 0):

                data['text'] = re.sub(r'[^\x00-\x7F]+', '', data['text'])
                url = re.compile(r"https?://\S+|www\.\S+")
                data['text'] = url.sub(r"", data['text'])

                mydata.append(data)


    df = pd.DataFrame.from_dict(mydata).reset_index()
    response_date = service.spreadsheets().values().update(
        spreadsheetId = spreadsheet_id,
        valueInputOption = 'RAW',
        range = range_name,
        body = dict(
            majorDimension = 'ROWS',
            values = df.T.reset_index().T.values.tolist())
    ).execute()
    print('Sheet successfully Updated')
