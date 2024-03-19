import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from dateutil.relativedelta import relativedelta, SU
from vars import calenderid

# If modifying these SCOPES, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']

def create_event(service, start_date, summary):
    end_date = start_date + datetime.timedelta(days=1)
    event_result = service.events().insert(calendarId=calenderid,
    body={
        "summary": summary,
        "description": summary,
        "start": {"date": start_date.strftime("%Y-%m-%d"), "timeZone": 'America/Los_Angeles'},
        "end": {"date": end_date.strftime("%Y-%m-%d"), "timeZone": 'America/Los_Angeles'},
        "reminders": {"useDefault": False},
    }).execute()

def main():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    service = build('calendar', 'v3', credentials=creds)

    # Calculate the last Sunday of each month for the next 12 months
    today = datetime.date.today()
    for i in range(12):
        month = today + relativedelta(months=+i)
        last_sunday = month + relativedelta(day=31, weekday=SU(-1))
        create_event(service, last_sunday, 'Family Day!')

if __name__ == '__main__':
    main()
