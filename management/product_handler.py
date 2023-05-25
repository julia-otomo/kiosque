from menu import products


def get_product_by_id(id):
    product_found = {}

    for product in products:
        if product.get("_id") == id:
            product_found = product.copy()
            return product_found

    return product_found


def get_products_by_type(type):
    products_list = []

    for product in products:
        if product.get("type") == type:
            products_list.append(product)

    return products_list


def add_product(menu: list, **kwargs):
    new_product = kwargs

    if len(menu) == 0:
        new_product["_id"] = 1
    else:
        id_list = []
        for product in menu:
            id_list.append(product["_id"])
        max_id = max(id_list)
        new_product["_id"] = max_id + 1

    menu.append(new_product)
    return new_product
