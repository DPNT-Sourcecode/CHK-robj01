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
    offer = ["A", "B"]
    cross_offer = ["E"]

    total_price = 0

    skus_counter = Counter(skus)
    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

    for item in cross_offer:

        price = price_table[item].price
        count = skus_counter[item]
        
        total_price += count * price





