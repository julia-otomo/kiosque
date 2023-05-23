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
