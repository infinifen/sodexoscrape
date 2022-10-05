import requests
from bs4 import BeautifulSoup

from scrape import restaurant_from_bs4


def get_restaurant_html(restaurant_id: int):
    url = f'https://enjoyyourmeal.pl/menu/restaurant/id/{restaurant_id}'
    html = requests.get(url)
    return html


def main():
    res = get_restaurant_html(36)
    bs = BeautifulSoup(res.text, features="lxml")
    print(restaurant_from_bs4(bs))


if __name__ == '__main__':
    main()
