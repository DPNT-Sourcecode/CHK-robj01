from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

class item:

    def __init__(self, name, price):
        self.name = name
        self.price = price

class A(item):
    def __init__(self, price):
        super().__init__(name, price)

class B(item):
    def __init__(self, price):
        super().__init__(name, price)

class C(item):
    def __init__(self, price):
        super().__init__(name, price)

class D(item):
    def __init__(self, price):
        super().__init__(name, price)

class E(item):
    def __init__(self, price):
        super().__init__(name, price)

def checkout(skus):

    price_table = {"A": A()},
                   "B": {"price": 30, "offer": {"count": 2, "price": 45}},
                   "C": {"price": 20, "offer": None},
                   "D": {"price": 15, "offer": None},
                   "E": {"price": 40, "offer": None},}

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

    return total_price





