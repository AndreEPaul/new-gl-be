import os
from flask import Flask, render_template, jsonify
import googleapiclient.discovery
from google.oauth2 import service_account
from fuzzywuzzy import fuzz, process
import webscraper

app = Flask(__name__)

# credit to "https://github.com/jessamynsmith/flask-google-sheets" for Google Sheets help

def get_credentials():
    scopes = ["https://www.googleapis.com/auth/spreadsheets.readonly"]
    GOOGLE_PRIVATE_KEY = os.environ["GOOGLE_PRIVATE_KEY"]

    account_info = {
      "private_key": GOOGLE_PRIVATE_KEY,
      "client_email": os.environ["GOOGLE_CLIENT_EMAIL"],
      "token_uri": "https://accounts.google.com/o/oauth2/token",
    }

    credentials = service_account.Credentials.from_service_account_info(account_info, scopes=scopes)
    return credentials

def get_service(service_name='sheets', api_version='v4'):
    credentials = get_credentials()
    service = googleapiclient.discovery.build(service_name, api_version, credentials=credentials)
    return service

@app.route('/', methods=['GET'])
def homepage():
    service = get_service()
    spreadsheet_id = os.environ["GOOGLE_SPREADSHEET_ID"]
    range_name = os.environ["GOOGLE_CELL_RANGE"]

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    owned_players = []

    for player in values:
        if(player != [] and player[2] != ''):
            owned_players.append(player[0])

    redraft_no_rookies = webscraper.get_redraft_no_rookies()

    for player in owned_players:
        redraftPlayerToRemove = process.extractOne(player, redraft_no_rookies)
        redraft_no_rookies.remove(redraftPlayerToRemove[0])

    # return jsonify(redraft_no_rookies)
    return render_template('index.html', values=values)

@app.route('/dynasty', methods=['GET'])
def dynasty_page():
    service = get_service()
    spreadsheet_id = os.environ["GOOGLE_SPREADSHEET_ID"]
    range_name = os.environ["GOOGLE_CELL_RANGE"]

    result = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()
    values = result.get('values', [])

    owned_players = []

    for player in values:
        if(player != [] and player[2] != ''):
            owned_players.append(player[0])

    dynasty_no_rookies = webscraper.get_dynasty_no_rookies()

    for player in owned_players:
        dynastyPlayerToRemove = process.extractOne(player, dynasty_no_rookies)
        dynasty_no_rookies.remove(dynastyPlayerToRemove[0])

    return jsonify(dynasty_no_rookies)

if __name__ == '__main__':
    app.run(debug=True)