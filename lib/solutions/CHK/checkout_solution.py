from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    class cross_offer:
        @staticmethod
        def apply(count):
            pass

    class offer:
        @staticmethod
        def apply(count):
            pass

class A(item):
    def __init__(self):
        super().__init__("A", 50)
class B(item):
    def __init__(self):
        super().__init__("B", 30)

class C(item):
    def __init__(self):
        super().__init__("C", 20)

class D(item):
    def __init__(self):
        super().__init__("D", 15)

class E(item):
    def __init__(self):
        super().__init__("E", 40)




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
        item_object.cross_offer.apply()











