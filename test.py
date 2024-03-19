from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)

    # Call the Calendar API
    print("Getting the upcoming 10 events")
    calendar_list = service.calendarList().list().execute()
    for calendar_list_entry in calendar_list['items']:
        print(calendar_list_entry['id'])

if __name__ == '__main__':
    main()
