import requests
from bs4 import BeautifulSoup as bs
import tokens


def get_income(period):
    """ Gets income per period from website's dashboard.

    Parameters:
    period(str): 'today' or 'yesterday'.

    Returns:
    str(pravoved_income) or prints error if login fails.
    """

    login_url = tokens.LOGIN_URL
    dashboard_url = tokens.DASHBOARD_URL.format(period)

    # Create session
    session = requests.Session()
    payload = tokens.PAYLOAD
    # Log in
    response = session.post(login_url, data=payload, headers=dict(referer=login_url))
    # Go to dashboard page
    response = session.get(dashboard_url)
    # Make soup if login was successful
    if 'Партнерская программа' in response.text:
        soup = bs(response.text, 'html.parser')
        itogo = soup.select('table > tbody > tr')
        # Find row with income
        i = itogo[-1].select('td')
        pravoved_income = int((i[-1].get_text().strip(' р.')))
        return str(pravoved_income)
    # Inform if login wasn't successful
    else:
        print('Not logged in')
