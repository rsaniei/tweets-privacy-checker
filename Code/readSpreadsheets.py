from __future__ import print_function
import pickle
import os.path
import json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# This script reads a sheet(range_name) of a google spreadsheet document(spreadsheet_id)
# and write the rows in a 'jsonl' format in a file (here corpus.jsonl)


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


def read_spreadsheet(spreadsheet_id, range_name):

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

        values = result.get('values', [])
        if not values:
            print('No data found.')
        else:
            for row in values:
                print(row[0])
                my_dict = {}
                with open('corpus.jsonl', 'a') as output:

                    my_dict["id"] = int(row[1])
                    my_dict["id_str"] = row[1]
                    my_dict["created_at"] = row[2]

                    if (row[0] == "TRUE"):
                        my_dict["ambiguous"] = 'true'

                    else:
                        if (row[3] == row[4] and row[4] == row[5] and row[3]=="NHS"):
                            my_dict["physical_health_sensitivity"] = row[4]
                        else:
                            if(row[3] == row[4] and row[4] == row[5] and row[3]=="HS"):
                                my_dict["physical_health_sensitivity"] = row[3]
                            else:
                                my_dict["physical_health_sensitivity_1"] = row[3]
                                my_dict["physical_health_sensitivity_2"] = row[4]
                                my_dict["physical_health_sensitivity_3"] = row[5]

                            if (row[7] == row[8] and row[8]== row[9] and (len(row[7])) != 0):
                                my_dict["type"] = row[7]
                            else:
                                if len(row[7]) != 0: my_dict["type_1"] = row[7]
                                if len(row[8]) != 0: my_dict["type_2"] = row[8]
                                if len(row[9]) != 0: my_dict["type_3"] = row[9]

                            if (row[11] == row[12] and row[12] == row[13] and len(row[11]) != 0):
                                my_dict["subject"] = row[12]
                            else:
                                if len(row[11]) != 0: my_dict["subject_1"] = row[11]
                                if len(row[12]) != 0: my_dict["subject_2"] = row[12]
                                if len(row[13]) != 0: my_dict["subject_3"] = row[13]


                    output.write((json.dumps(my_dict).encode('utf8') + b"\n").decode('utf8'))
    except Exception as e:
        print(e)

    print('Read Sheet successfully')
