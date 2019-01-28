import os

CRED_FILE = '{}{}'.format(os.getcwd(), '/google_api_credentials.json')

# Yandex
# OAuth-токен пользователя, от имени которого будут выполняться запросы
TOKEN = ''
LOGIN = ''
MASTER_TOKEN = ''

# Pravoved
LOGIN_URL = 'https://pravoved.ru/login/'
DASHBOARD_URL = 'https://pravoved.ru/private/affiliate/?range={}'
PAYLOAD = {
    'email': '',
    'password': '',
    'loginform': '1',
}
# GoogleSheets
SPREADSHEET_URL = ''

# Lexprofit
LEX_URL = 'https://lexprofit.ru/auth/login'
EMAIL = ''
PASSWORD = ''
