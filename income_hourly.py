#! /usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import date
from time import sleep
import gspread
import tokens, pravoved_data, yandex_data
from oauth2client.service_account import ServiceAccountCredentials


def main():
    while True:
        pr_income = pravoved_data.get_income('today')
        ya_spend = yandex_data.get_expenses('TODAY')
        write_to_spreadsheet(pr_income, ya_spend)
        sleep(3600)

def authorize():
    # Gspread authorize
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                  'google_api_credentials.json',
                  scope
                  )
    return gspread.authorize(credentials)

def write_to_spreadsheet(pr_income, ya_spend):
    # Get date
    today = date.today().strftime('%d.%m')
    gc = authorize()
    # Open worksheet and write hourly data
    try:
        spreadsheet = gc.open_by_url(tokens.spreadsheet_url)
        worksheet = spreadsheet.worksheet('hourly')
        last_row = worksheet.row_count
        date_column = worksheet.cell(last_row, 1).value.split()
        # Check if date in the last row is today
        if today in date_column:
            worksheet.update_cell(last_row, 3, pr_income)
            worksheet.update_cell(last_row, 5, ya_spend)
        else:
            print('date is not today')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet was not opened')


if __name__ == '__main__':
    main()
