from menu import products
from collections import Counter
import functools


def get_product_by_id(id: int):
    if not isinstance(id, int):
        raise TypeError("product id must be an int")

    product_found = {}

    for product in products:
        if product.get("_id") == id:
            product_found = product.copy()
            return product_found

    return product_found


def get_products_by_type(type: str):
    if not isinstance(type, str):
        raise TypeError("product type must be a str")

    products_list = []

    for product in products:
        if product.get("type") == type:
            products_list.append(product)

    return products_list


def add_product(menu: list, **kwargs):
    new_product = kwargs
    new_product["_id"] = 0

    if len(menu) == 0:
        new_product["_id"] += 1
    else:
        id_list = []
        for product in menu:
            id_list.append(product["_id"])
        max_id = max(id_list)
        new_product["_id"] = max_id + 1

    menu.append(new_product)
    return new_product


def menu_report():
    product_count = len(products)

    prices_list = [price["price"] for price in products]
    average_price = (functools.reduce(lambda a, b: a + b, prices_list)) / len(
        prices_list
    )
    types_list = [type["type"] for type in products]
    most_common_type = Counter(types_list).most_common(1)[0][0]

    result_phrase = f"Products Count: {product_count} - Average Price: ${round(average_price, 2)} - Most Common Type: {most_common_type}"

    return result_phrase


def add_product_extra(menu: list, *necessary_keys: list, **new_product: dict):
    for key in necessary_keys:
        if key not in new_product.keys():
            raise KeyError(f"Field '{key}' is required")

    new_product_menu = {
        key: value for key, value in new_product.items() if key in necessary_keys
    }

    product_id = max((product["_id"] for product in menu), default=0)

    new_product_menu["_id"] = product_id + 1

    menu.append(new_product)

    return new_product_menu
