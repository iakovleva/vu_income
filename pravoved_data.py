#! /usr/bin/python3
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup as bs
import tokens


def get_income(period):
    login_url = tokens.login_url
    dashboard_url = tokens.dashboard_url.format(period)
    s = requests.Session()
    payload = tokens.payload

    response = s.post(login_url, data=payload, headers=dict(referer=login_url))
    response = s.get(dashboard_url)
    if 'Партнерская программа' in response.text:
        soup = bs(response.text, 'html.parser')
        itogo = soup.select('table > tbody > tr')
        i = itogo[-1].select('td')
        pravoved_income = int((i[-1].get_text().strip(' р.')))
        return str(pravoved_income)
    else:
        print('Not logged in')
