from collections import Counter


# noinspection PyUnusedLocal
# skus = unicode string


def checkout(skus):
    class item:
        def __init__(self, name, price, count=0):
            self.name = name
            self.price = price
            self.count = count

        def total_price(self):
            return self.price * max(self.count, 0)

        def cross_offer(self):
            return None

    class A(item):
        def __init__(self, price, count):
            super().__init__("A", price, count)

        def total_price(self):
            count = self.count
            total_price = 0

            total_price += (count // 5) * 200

            count = count % 5
            total_price += (count // 3) * 130

            count = count % 3
            total_price += count * 50
            return total_price

    class B(item):
        def __init__(self, price, count):
            super().__init__("B", price, count)

        def total_price(self):
            count = max(self.count, 0)
            total_price = 0

            total_price += (count // 2) * 45

            count = count % 2
            total_price += count * 30

            return total_price

    class C(item):
        def __init__(self, price, count):
            super().__init__("C", price, count)

    class D(item):
        def __init__(self, price, count):
            super().__init__("D", price, count)

    class E(item):
        def __init__(self, price, count):
            super().__init__("E", price, count)

        def cross_offer(self):
            B.count -= (E.count // 2)

    skus_counter = Counter(skus)

    A = A(price=50, count=skus_counter["A"])
    B = B(price=50, count=skus_counter["B"])
    C = C(price=50, count=skus_counter["C"])
    D = D(price=50, count=skus_counter["D"])
    E = E(price=50, count=skus_counter["E"])
    F = F(price=50, count=skus_counter["F"])

    items_table = {"A": A,
                   "B": B,
                   "C": C,
                   "D": D,
                   "E": E}

    for item, count in skus_counter.items():
        if item not in items_table.keys(): return -1
        items_table[item].cross_offer()

    basket_value = 0
    for item in items_table.values():
        basket_value += item.total_price()

    return basket_value
