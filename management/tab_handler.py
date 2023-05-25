from menu import products
import functools


def calculate_tab(table: list):
    payment_list = []
    resulted_dict = {}

    for product in products:
        for item in table:
            if item["_id"] == product["_id"]:
                separate_payment = item["amount"] * product["price"]
                payment_list.append(separate_payment)

    completed_payment = functools.reduce(lambda a, b: a + b, payment_list)

    resulted_dict["subtotal"] = f"${round(completed_payment, 2)}"
    return resulted_dict


calculate_tab([{"_id": 1, "amount": 5}, {"_id": 19, "amount": 5}])
