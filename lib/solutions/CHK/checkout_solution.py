from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string

class offer:

    def __init__(self, single, multi):
        self.single = single
        self.multi = multi

class A(offer):
    def __init__(self):
        self.price = 50
        super().__init__(single=True, multi=False)

class B(offer):
    def __init__(self):
        self.price = 30
        super().__init__(single=True, multi=False)

class C(offer):
    def __init__(self):
        self.price = 20
        super().__init__(single=False, multi=False)

class D(offer):
    def __init__(self):
        self.price = 15
        super().__init__(single=False, multi=False)

class E(offer):
    def __init__(self):
        self.price = 40
        super().__init__(single=False, multi=True)


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







