import gspread
import tokens, gspread_authorize
from collections import Counter


def matreshka_income():
    """ Parse 2 spreadsheets: 
    
    Income - where all data about income and expenses stored.
    Matreshka - data about orders from partner.
    Result: add 1100 to the Income cell with the date when the order was
    registered.
    """

    # Authorization required by Google API
    gc = gspread_authorize.authorize()
    
    # Open Matreshka spreadsheet
    ws_matreshka = gspread_authorize.open_sheet(
        gc, 
        tokens.SPREADSHEET_MATRESHKA,
        'Пришедшие (света)')

    # Open Income worksheet
    ws_income = gspread_authorize.open_sheet(
        gc,
        tokens.SPREADSHEET_INCOME,
        'daily')
  
    # Count rows in Matreshka sheet
    number_of_rows = len(ws_matreshka.col_values(1))
    dates = []

    # Get dates from all new rows in Matreshka sheet
    for i in range(number_of_rows-1):
        date = ws_matreshka.cell(i+2, 7).value.split()[0]
        dates.append(date)
    
    # Count all occurences of each date 
    dates_counter = Counter(dates)

    # Write income to the rows with appropriate dates in Income sheet
    for date in dates_counter.keys():
        date_cell = ws_income.find('{}'.format(date))
        # If date=today, it's not in Income sheet yet
        if date_cell:
            ws_income.update_cell(date_cell.row, 4, dates_counter[date]*1100)


if __name__=='__main__':
     matreshka_income()
