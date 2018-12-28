from datetime import date, timedelta
import gspread
import tokens, pravoved_data, yandex_data, lex_data, gspread_authorize


def main():
    """
    Runs scripts that gets income and expenses
    in order to write this information to spreadsheet.
    """

    pr_income = pravoved_data.get_income('yesterday')
    lex_income = lex_data.get_income(2)
    ya_spend = yandex_data.get_expenses('YESTERDAY')
    write_to_spreadsheet(pr_income, lex_income, ya_spend)


def write_to_spreadsheet(pr_income, lex_income, ya_spend):
    """Writes data to spreadsheet. """

    # Get date
    today = date.today()
    delta = timedelta(days=1)
    yesterday = (today - delta).strftime('%d.%m.%y')

    # Gspread authorize
    gc = gspread_authorize.authorize()

    # Open worksheet and write daily data
    try:
        spreadsheet = gc.open_by_url(tokens.SPREADSHEET_URL)
        worksheet = spreadsheet.worksheet('daily')
        date_cell = worksheet.find('{}'.format(yesterday))
        if date_cell and ya_spend and pr_income and lex_income:
            worksheet.update_cell(date_cell.row, 2, lex_income)
            worksheet.update_cell(date_cell.row, 3, pr_income)
            worksheet.update_cell(date_cell.row, 5, ya_spend)
        else:
            worksheet.update_cell(date_cell.row, 2, 'No data')
            worksheet.update_cell(date_cell.row, 3, 'No data')
            worksheet.update_cell(date_cell.row, 5, 'No data')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet was not opened')


if __name__ == '__main__':
    main()
