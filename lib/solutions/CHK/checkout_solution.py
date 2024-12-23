from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string



def checkout(skus):

    class item:
        def __init__(self, name, price):
            self.name = name
            self.price = price
            self.count = 0

        @staticmethod
        def offer():
            return None

        @staticmethod
        def cross_offer():
            return None

    class A(item):
        def __init__(self):
            super().__init__("A", 50)

        @staticmethod
        def offer():
            count = A.count
            total_item_value = 0

            total_item_value += (count // 5) * 200

            count = count % 5
            total_item_value += (count // 3) * 130

            count = count % 3
            total_item_value += count * 50
            return total_item_value

    class B(item):
        def __init__(self):
            super().__init__("B", 30)

        @staticmethod
        def get(count):
            total_item_value = 0

            total_item_value += (count // 2) * 45

            count = count % 2
            total_item_value += count * 30

            return total_item_value

    class C(item):
        def __init__(self):
            super().__init__("C", 20)

    class D(item):
        def __init__(self):
            super().__init__("D", 15)

    class E(item):
        def __init__(self):
            super().__init__("E", 40)

        @staticmethod
        def cross_offer():
            B.count -= 1

    A, B, C, D, E = A(), B(), C(), D(), E()

    price_table = {"A": A,
                   "B": B,
                   "C": C,
                   "D": D,
                   "E": E}

    skus_counter = Counter(skus)
    for item, count in skus_counter.items():
        if item not in price_table.keys(): return -1

        item_object = price_table[item]
        item_object.count = count
        item_object.cross_offer()

    basket_value = 0
    for item in skus_counter.values():

    return basket_value








