#! /usr/bin/python3
# -*- coding: utf-8 -*-

from selenium import webdriver
import tokens


def get_income(period):
    # period arg: 1 = today, 2 = yesterday

    lex_url = tokens.lex_url
    driver = webdriver.Firefox()
    driver.get(lex_url)
    # Use by xpath because there are no id and name of elements
    email = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[1]/input")
    password = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/div[2]/input")
    email.send_keys(tokens.email)
    password.send_keys(tokens.password)
    submit = driver.find_element_by_xpath('/html/body/div[2]/div/div/form/button')
    submit.submit()
    # Wait while driver uploads redirect page
    driver.implicitly_wait(10)
    income = driver.find_element_by_xpath(
        '/html/body/div[1]/div[3]/div[3]/div[2]/div[2]/table/tbody/tr[{}]/td[5]'.format(period)
        )
    income = income.text.strip(' руб.')
    income = float(income.replace(',', '.'))
    driver.close()
    return income
