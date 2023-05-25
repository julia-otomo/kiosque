from management.product_handler import (
    add_product,
    get_products_by_type,
    get_product_by_id,
    menu_report,
)

from management.tab_handler import calculate_tab

from menu import products

if __name__ == "__main__":
    # Seus prints de teste aqui
    print(get_product_by_id(28))
    print(get_products_by_type("drink"))
    print(
        add_product(
            products,
            **{
                "title": "X-Python",
                "price": 5.0,
                "rating": 5,
                "description": "Sanduiche de Python",
                "type": "fast-food",
            }
        )
    )
    print(calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}]))
    print(
        calculate_tab(
            [
                {"_id": 10, "amount": 3},
                {"_id": 20, "amount": 2},
                {"_id": 21, "amount": 5},
            ]
        )
    )
    print(menu_report())
