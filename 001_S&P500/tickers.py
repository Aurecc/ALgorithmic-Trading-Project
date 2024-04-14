import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_tickers():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    response = requests.get(url)

    soup = BeautifulSoup(response.content, 'html.parser')

    stocks = (soup.find('tbody').find_all('tr'))[1:]

    stock_list = [stock.find('a').text for stock in stocks]
    stock_data= {'Ticker': stock_list}
    df = pd.DataFrame(stock_data)
    return df

