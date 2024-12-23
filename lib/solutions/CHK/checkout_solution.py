from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

class item:

    def __init__(self, name, price):
        self.name = name
        self.price = price


def checkout(skus):

    price_table = [item("A",50),
                   item("B",30),
                   item("C",20),
                   item("D",15),
                   item("E",40)]

    """
        total_price = 0

    skus_counter = Counter(skus)

    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

        item_price = price_table[item]["price"]

        if not price_table[item]["offer"]:
            total_price += item_price * count
        else:
            offer_count = price_table[item]["offer"]["count"]
            offer_price = price_table[item]["offer"]["price"]

            total_price += (count//offer_count) * offer_price + (count%offer_count) * item_price
    """

    print(price_table[0].name)
    return None







