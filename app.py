from flask import Flask, request, render_template, jsonify
import os
from google.oauth2 import service_account
from googleapiclient.discovery import build

app = Flask(__name__)

# Path to your service account file from an environment variable
SERVICE_ACCOUNT_FILE = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID and range of the Google Sheet
SPREADSHEET_ID = '1lH74N-02pvkp5maEqlvdY6fmdMUm3o_r9WGiFZcQP3M'
RANGE_NAME = 'Sheet1!A:A'

# Function to append data to Google Sheet
def append_to_sheet(email):
    service = build('sheets', 'v4', credentials=credentials)
    sheet = service.spreadsheets()
    values = [[email]]
    body = {'values': values}
    result = sheet.values().append(
        spreadsheetId=SPREADSHEET_ID,
        range=RANGE_NAME,
        valueInputOption='RAW',
        body=body
    ).execute()
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['email']
        if email:
            append_to_sheet(email)
            return jsonify(message="Thank you for joining the waitlist!", success=True)
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7001))
    app.run(debug=True, host='0.0.0.0', port=port)
