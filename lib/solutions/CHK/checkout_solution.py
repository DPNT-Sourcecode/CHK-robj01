from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

class A:
    def __init__(self):
        self.price = 50
        self.offer = True
        self.multi_offer = False

class B:
    def __init__(self):
        self.price = 30
        self.offer = True
        self.multi_offer = False

class C:
    def __init__(self):
        self.price = 20
        self.offer = True
        self.multi_offer = False

class D:
    def __init__(self):
        self.price = 15
        self.offer = True
        self.multi_offer = False

class E:
    def __init__(self):
        self.price = 40
        self.offer = False
        self.multi_offer = False


def checkout(skus):

    price_table = {"A": A(),
                   "B": B(),
                   "C": C(),
                   "D": D(),
                   "E": E()}

    total_price = 0

    skus_counter = Counter(skus)
    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

    for item in cross_offer:

        price = price_table[item].price
        count = skus_counter[item]

        total_price += count * price






