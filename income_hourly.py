from datetime import date
import tokens, pravoved_data, yandex_data, lex_data, gspread_authorize


def main():
    """
    Run scripts that gets income and expenses
    in order to write this information to spreadsheet.
    """

    pr_income = pravoved_data.get_income('today')
    lex_income = lex_data.get_income(1)
    ya_spend = yandex_data.get_expenses('TODAY')
    write_to_spreadsheet(pr_income, lex_income, ya_spend)


def write_to_spreadsheet(pr_income, lex_income, ya_spend):
    """Write data to spreadsheet."""

    # Get date
    today = date.today().strftime('%d.%m')
    gc = gspread_authorize.authorize()
    # Open worksheet 
    worksheet = gspread_authorize.open_sheet(
        gc, 
        tokens.SPREADSHEET_INCOME,
        'hourly')
    date_column = worksheet.cell(2, 1).value.split()
    # Check if date in the first row is today
    if today in date_column:
        # Write hourly data
        worksheet.update_cell(2, 2, lex_income)
        worksheet.update_cell(2, 3, pr_income)
        worksheet.update_cell(2, 5, ya_spend)
    else:
        print('date is not today')


if __name__ == '__main__':
    main()
