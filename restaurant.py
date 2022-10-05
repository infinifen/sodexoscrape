from dataclasses import dataclass

from bs4 import BeautifulSoup


@dataclass(init=True, repr=True)
class Meal:
    name: str
    kind: str # might be replaced by specific properties for stuff like containing meat, regular/light etc. later


@dataclass(init=True, repr=True)
class Category:
    name: str
    meals: list[Meal]


@dataclass(init=True, repr=True)
class Restaurant:
    id: int
    name: str
    address: str
    categories: list[Category]
