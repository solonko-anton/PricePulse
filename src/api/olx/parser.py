from bs4 import BeautifulSoup
import requests

def parse_fridgers():
    url = 'https://www.olx.ua/uk/list/q-%D0%A5%D0%BE%D0%BB%D0%BE%D0%B4%D0%B8%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%B8/'
    page = requests.get(url)

    soup = BeautifulSoup(page.text, 'html.parser')

    fridges = [
                {
                    "name": obj.find('h4', class_='css-1g61gc2').text,
                    "price" : obj.find('p', class_='css-uj7mm0').text,
                    'url': 'https://www.olx.ua/' + obj.find('a', class_='css-1tqlkj0').get('href')
                } 
                    for obj in soup.find_all('div', class_='css-l9drzq')
                    if obj.find('p', class_='css-uj7mm0') is not None
            ]

    return fridges