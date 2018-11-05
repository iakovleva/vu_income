# -*- coding: utf-8 -*-

from datetime import date, timedelta
from time import sleep
import gspread
import tokens, pravoved_data, yandex_data
from oauth2client.service_account import ServiceAccountCredentials


def main():
    while True:
        pr_income = pravoved_data.get_income('yesterday')
        ya_spend = yandex_data.get_expenses('YESTERDAY')
        write_to_spreadsheet(pr_income, ya_spend)
        sleep(3600*24)

def authorize():
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                  'google_api_credentials.json',
                  scope
                  )
    return gspread.authorize(credentials)

def write_to_spreadsheet(pr_income, ya_spend):
    # Get date
    today = date.today()
    delta = timedelta(days=1)
    yesterday = (today - delta).strftime('%d.%m.%y')

    # Gspread authorize
    gc = authorize()

    # Open worksheet and write daily data
    try:
        spreadsheet = gc.open_by_url(tokens.spreadsheet_url)
        worksheet = spreadsheet.worksheet('daily')
        date_cell = worksheet.find('{}'.format(yesterday))
        if date_cell and ya_spend and pr_income:
            worksheet.update_cell(date_cell.row, 3, pr_income)
            worksheet.update_cell(date_cell.row, 5, ya_spend)
        else:
            worksheet.update_cell(date_cell.row, 3, 'No data')
            worksheet.update_cell(date_cell.row, 5, 'No data')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet was not opened')


if __name__ == '__main__':
    main()
