import requests
import csv
import pandas as pd
from bs4 import BeautifulSoup
from datetime import datetime


def collect_data():
    """
    Header parsing function from 'habr.com'!
    """
    headlines_collection = []
    count_page = 1
    t_date = datetime.now().strftime('%d_%m_%Y')

    responce = requests.get('https://habr.com/ru/all/')
    soup = BeautifulSoup(responce.text, 'lxml')
    quotes = soup.find_all('a', class_='tm-article-snippet__title-link')
    headlines_collection += quotes

    while count_page < 51:
        responce = requests.get(f'https://habr.com/ru/all/page{count_page}/')
        soup = BeautifulSoup(responce.text, 'lxml')
        quotes = soup.find_all('a', class_='tm-article-snippet__title-link')
        headlines_collection += quotes
        count_page += 1

    data = [head.text for head in headlines_collection]

    df = pd.DataFrame({'Аrticle titles': data})
    df.to_excel(f'./parsing_data/titles(xlsx)_{t_date}.xlsx', index=False)

    print(f'Parsing done - {t_date}!')


def main():
    collect_data()


if __name__ == '__main__':
    main()
