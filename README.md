# VU_Income

Regularly collects data from Yandex Direct and Pravoved website. Stores
this data in Google Spreadsheet. 

Income_daily.py collects data once a day.
Income_hourly.py runs every hour.

### Prerequisites

Script uses:
- Yandex Direct API
- Beautifulsoup and python requests module to scrape Pravoved website
- Selenium for scraping Lexprofit website
- Gspread for authorization in Google SpreadSheets

## Getting Started

1. Create Google SpreadSheet
2. In SpreadSheet:
   - Create 2 tabs called 'hourly', 'daily'.
   - In the first column of 'daily' tab write yesterday's date, i.e. '08.01.18'
   - In the first column of 'hourly' tab write today's date and time, i.e. '09.01 12:00'

3. Create project

```
mkdir income
cd income
(create virtualenv)
git clone https://github.com/iakovleva/vu_income
cd vu_income
pip install -r requirements.txt
```

4. Get Google API credentials for Gspread authorize. 
(Save Google API credentials file in the current directory) 
5. Fill in tokens.py file.  
6. Run script

```
python income_daily.py
python income_hourly.py
```

