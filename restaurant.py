from dataclasses import dataclass, field

from bs4 import BeautifulSoup


@dataclass(init=True, repr=True)
class Meal:
    name: str = ''
    english_name: str = ''
    kind: str = ''  # might be replaced by specific properties for stuff like containing meat, regular/light etc. later


@dataclass(init=True, repr=True)
class Category:
    name: str = ''
    meals: list[Meal] = field(default_factory=list)

    def __iter__(self):
        return self.meals.__iter__()


@dataclass(init=True, repr=True)
class Restaurant:
    id: int
    name: str
    address: str
    categories: list[Category]

    def __iter__(self):
        return self.categories.__iter__()
