from datetime import date, timedelta
import tokens, pravoved_data, yandex_data, lex_data, gspread_authorize


def main():
    """
    Run scripts that gets income and expenses
    in order to write this information to spreadsheet.
    """

    pr_income = pravoved_data.get_income('yesterday')
    lex_income = lex_data.get_income(2)
    ya_spend = yandex_data.get_expenses('YESTERDAY')
    write_to_spreadsheet(pr_income, lex_income, ya_spend)


def write_to_spreadsheet(pr_income, lex_income, ya_spend):
    """Write data to spreadsheet."""

    # Get date
    today = date.today()
    delta = timedelta(days=1)
    yesterday = (today - delta).strftime('%d/%m/%Y')

    # Gspread authorize
    gc = gspread_authorize.authorize()

    # Open worksheet 
    worksheet = gspread_authorize.open_sheet(
        gc, 
        tokens.SPREADSHEET_INCOME,
        'daily')
    date_cell = worksheet.find('{}'.format(yesterday))
    if date_cell and ya_spend:
    # if pr_income and lex_income:
        worksheet.update_cell(date_cell.row, 2, lex_income)
        worksheet.update_cell(date_cell.row, 3, pr_income)
        worksheet.update_cell(date_cell.row, 6, ya_spend)
    else:
        worksheet.update_cell(date_cell.row, 2, 'No data')
        worksheet.update_cell(date_cell.row, 3, 'No data')
        worksheet.update_cell(date_cell.row, 6, 'No data')


if __name__ == '__main__':
    main()
