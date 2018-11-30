#! /usr/bin/python3
# -*- coding: utf-8 -*-

from datetime import date, datetime
import gspread
import tokens, pravoved_data, yandex_data
from oauth2client.service_account import ServiceAccountCredentials


def main():
    pr_income = pravoved_data.get_income('today')
    ya_spend = yandex_data.get_expenses('TODAY')
    write_to_spreadsheet(pr_income, ya_spend)
    print(datetime.datetime.now())

def authorize():
    # Gspread authorize
    scope = ['https://spreadsheets.google.com/feeds']
    cred_file = tokens.cred_file
    credentials = ServiceAccountCredentials.from_json_keyfile_name(
                  cred_file,
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
        date_column = worksheet.cell(2, 1).value.split()
        # Check if date in the first row is today
        if today in date_column:
            worksheet.update_cell(2, 3, pr_income)
            worksheet.update_cell(2, 5, ya_spend)
        else:
            print('date is not today')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet was not opened')


if __name__ == '__main__':
    main()
