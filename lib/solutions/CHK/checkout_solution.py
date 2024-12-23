from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

class offer:

    def __init__(self, single, multi):
        self.single = single
        self.multi = multi

class A():
    def __init__(self):
        self.price = 50
        self.offer = offer(single=True, multi=False)

class B():
    def __init__(self):
        self.price = 30
        self.offer = offer(single=True, multi=False)

class C():
    def __init__(self):
        self.price = 20
        self.offer = offer(single=False, multi=False)

class D():
    def __init__(self):
        self.price = 15
        self.offer = offer(single=False, multi=False)

class E():
    def __init__(self):
        self.price = 40
        self.offer = offer(single=False, multi=True)


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

        item_object = price_table[item]
        if item_object.price > total_price:








