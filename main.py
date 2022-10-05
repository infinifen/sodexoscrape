import requests
from bs4 import BeautifulSoup


def get_restaurant_html(restaurant_id: int):
    url = f'https://enjoyyourmeal.pl/menu/restaurant/id/{restaurant_id}'
    print(url)
    html = requests.get(url)
    return html


def main():
    res = get_restaurant_html(36)
    bs = BeautifulSoup(res.text, features="lxml")
    print(bs)


if __name__ == '__main__':
    main()
