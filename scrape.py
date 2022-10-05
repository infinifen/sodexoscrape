from bs4 import BeautifulSoup

from restaurant import Restaurant, Category, Meal


def restaurant_from_bs4(bs: BeautifulSoup) -> Restaurant:
    restaurant_name = bs.h1.a.text
    restaurant_addr = bs.p.text
    restaurant_div = bs.find(class_='restaurant')
    menu = bs.find(class_='restaurant-menu')
    cat_list = parse_menu(menu)
    return Restaurant(0, restaurant_name, restaurant_addr, cat_list)


def parse_menu(menu: BeautifulSoup) -> list[Category]:
    cat_list: list[Category] = []
    current_cat: Category | None = None
    current_meal: Meal | None = None
    for tag in menu.children:
        match tag.name:
            case 'h2':
                if current_cat is not None:  # no previous category ever existed
                    cat_list.append(current_cat)

                current_cat = Category(name=tag.text)

            case 'h3':
                if current_meal is not None:  # no previous meal ever existed
                    current_cat.meals.append(current_meal)

                current_meal = Meal(name=tag.text)

            case 'h4':
                current_meal.english_name = tag.text

            case 'p':
                current_meal.kind = tag.text

    return cat_list
