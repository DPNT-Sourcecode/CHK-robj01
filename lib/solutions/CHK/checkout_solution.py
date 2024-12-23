from collections import Counter

# noinspection PyUnusedLocal
# skus = unicode string
class item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    class cross_offer:
        @staticmethod
        def get(count):
            return None

    class offer:
        @staticmethod
        def get(count):
            return None

class A(item):
    def __init__(self):
        super().__init__("A", 50)
        self.count = 0

    class offer:
        @staticmethod
        def get():
            count = A.count
            total_item_value = 0

            total_item_value += (count//5) * 200

            count = count%5
            total_item_value += (count//3) * 130

            count = count%3
            total_item_value += count * 50
            return total_item_value
class B(item):
    def __init__(self):
        super().__init__("B", 30)

    class offer:
        @staticmethod
        def get(count):
            total_item_value = 0

            total_item_value += (count//2) * 45

            count = count%2
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
        item_object.count = count

        print(item_object.count)







