import gspread
import tokens, gspread_authorize


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
    try:
        ss_matreshka = gc.open_by_url(tokens.SPREADSHEET_MATRESHKA)
        ws_matreshka = ss_matreshka.worksheet('Пришедшие')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet Matreshka was not opened')

    # Open worksheet and write daily data
    try:
        ss_income = gc.open_by_url(tokens.SPREADSHEET_INCOME)
        ws_income = ss_income.worksheet('daily')
    except gspread.exceptions.GSpreadException as e:
        print(e)
    except:
        print('Spreadsheet Income was not opened')
  
    # Count rows in Matreshka sheet
    number_of_rows = len(ws_matreshka.col_values(1))
    # Get the number of rows after previous run
    previous_rows = int(ws_income.cell(1, 16).value)
    dates = []

    # Get dates from all new rows in Matreshka sheet
    for i in range(number_of_rows - previous_rows):
        date = ws_matreshka.cell(i+2, 7).value.split()[0]
        previous_rows += 1
        dates.append(date)
    # Update number of rows for the next run
    ws_income.update_cell(1, 16, previous_rows)

    # Write income to the rows with appropriate dates in Income sheet
    for date in dates:
        date_cell = ws_income.find('{}'.format(date))
        # If date=today, it's not in Income sheet yet
        if date_cell:
            cell = ws_income.cell(date_cell.row, 4).value
            if cell is '':
                ws_income.update_cell(date_cell.row, 4, '1100')
            else:
                ws_income.update_cell(date_cell.row, 4, int(cell)+1100)

if __name__=='__main__':
     matreshka_income()
