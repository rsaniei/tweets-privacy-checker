from __future__ import print_function
import pickle
import os.path
import re
import ast
import pandas as pd
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# The ID and range of a sample spreadsheet.
# SAMPLE_SPREADSHEET_ID = '1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms'
SAMPLE_SPREADSHEET_ID = '1Jvw5gEe8Zt5hszvdlMcHcL3VNFJN-lt9dWZ_BV3O5B0'
SAMPLE_RANGE_NAME = 'Sheet6-1!A1:P'

def main():
    """Shows basic usage of the Sheets API.
    Prints values from a sample spreadsheet.
    """
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
        result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                    range=SAMPLE_RANGE_NAME).execute()
        # return service
    except Exception as e:
        print(e)
        # return None

    with open('pattern6-noRT.txt', 'r') as f:
        mydata = []
        for line in f:
            data = ast.literal_eval(line)
            data['text'] = re.sub("(@[A-Za-z0-9]+(:)?)|(RT)","", data['text'])
            data['text'] = re.sub(r'[^\x00-\x7F]+', '', data['text'])

            mydata.append(data)


    df = pd.DataFrame.from_dict(mydata).reset_index()
    response_date = service.spreadsheets().values().update(
        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        valueInputOption='RAW',
        range=SAMPLE_RANGE_NAME,
        body=dict(
            majorDimension='ROWS',
            values= df.T.reset_index().T.values.tolist())
    ).execute()
    print('Sheet successfully Updated')

    # read values in the spreadsheet
    # values = result.get('values', [])
    # # print(values)
    #
    # if not values:
    #     print('No data found.')
    # else:
    #     print('File has some value!')





if __name__ == '__main__':
    main()