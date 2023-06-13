# Parsing articles from habr
This project is dedicated to the topic of [data parsing](https://oxylabs.io/blog/what-is-data-parser).

if you have any questions you can ask me on mail: mmigur@bk.ru

Scroll down to view the repository

# Table of Contents
* Description
* Installation and launch of the project
* My progress

# Description
In this project I tried to use basic knowledge of python and libraries for data parsing:
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)
* [Requests](https://python-scripts.com/requests)

Next, I moved on to writing the code and created the main function:
```python
import requests
import csv # write csv file.
import pandas as pd # library work data frame.
from bs4 import BeautifulSoup # parsing library.
from datetime import datetime

def main():
    collect_data()


if __name__ == '__main__': 
    main()
```

Then I proceeded to the main functionality
Wrote an algorithm for parsing by tags

```python
responce = requests.get('https://habr.com/ru/all/')
soup = BeautifulSoup(responce.text, 'lxml')
quotes = soup.find_all('a',class_='tm-article-snippet__title-link')
headlines_collection += quotes
```

But there was a problem that it parsed only the first page of the article, and I solved this problem. I started a variable where I wrote the number of pages and substituted it into the string in the loop

```python
count_page = 1
max_count_page = 51

while count_page < max_count_page:
    responce = requests.get(f'https://habr.com/ru/all/page{count_page}/')
    soup = BeautifulSoup(responce.text, 'lxml')
    quotes = soup.find_all('a', class_='tm-article-snippet__title-link')
    headlines_collection += quotes
    count_page += 1
```
And finally, I wrote it all down in an excel file
```python
    df = pd.DataFrame({'Аrticle titles': data})
    df.to_excel(f'./parsing_data/titles(xlsx)_{t_date}.xlsx', index=False)
```
# Installation and launch of the project 
* First we need to install the python interpreter from the [official website](https://www.python.org/downloads/)
* Open the console and enter the commands to install the libraries there:
  * *pip install pandas*
  * *pip install beautifulsoup4*
* Open the code in any code editor and run

# My progress

In the future, I want to work in the field of data analysis and for this I post projects. Although they are simple, but I am learning something.
