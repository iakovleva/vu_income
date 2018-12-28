import gspread
from oauth2client.service_account import ServiceAccountCredentials
import tokens


def authorize():
    """Makes authorization in a Google Spreadsheet """

    # Gspread authorize
    scope = ['https://spreadsheets.google.com/feeds']
    cred_file = tokens.CRED_FILE
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
        cred_file,
        scope
        )
    return gspread.authorize(credentials)
