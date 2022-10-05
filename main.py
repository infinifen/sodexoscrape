import sys

import requests
from bs4 import BeautifulSoup
from rich import print
from rich.tree import Tree

from restaurant import Restaurant
from scrape import restaurant_from_bs4


def get_restaurant_html(restaurant_id: int):
    url = f'https://enjoyyourmeal.pl/menu/restaurant/id/{restaurant_id}'
    html = requests.get(url)
    return html


def build_restaurant_tree(r: Restaurant) -> Tree:
    tree = Tree(r.name, style="bold")
    for cat in r:
        cat_subtree = tree.add(cat.name, style="not bold green")
        for meal in cat:
            meal_str = f'[default]{meal.name}[/] [bright_black]{meal.kind}[/]'
            cat_subtree.add(meal_str)
    return tree


def main(restaurant_id: int):
    res = get_restaurant_html(restaurant_id)
    bs = BeautifulSoup(res.text, features="lxml")
    restaurant = restaurant_from_bs4(bs)
    tree = build_restaurant_tree(restaurant)
    print(tree)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("error: no restaurant id provided", file=sys.stderr)
        exit(1)
    else:
        try:
            rid = int(sys.argv[1])
        except ValueError:
            print("error: restaurant id is not an integer", file=sys.stderr)
            exit(1)
        else:
            main(rid)
