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

    class two_level_offer_item(item):
        def __init__(self, name, price, count, first_offer_count, first_offer_price, second_offer_count, second_offer_price):
            super().__init__(name, price, count)

            self.first_offer_count = first_offer_count
            self.first_offer_price = first_offer_price
            self.second_offer_count = second_offer_count
            self.second_offer_price = second_offer_price

        def total_price(self):
            count = max(self.count, 0)
            total_price = 0

            total_price += (count // self.first_offer_count) * self.first_offer_price

            count = count % self.first_offer_count
            total_price += (count // self.second_offer_count) * self.second_offer_price

            count = count % self.second_offer_count
            total_price += count * self.price
            return total_price

    class one_level_offer_item(item):
        def __init__(self, name, price, count, offer_count, offer_price):
            super().__init__(name, price, count)

            self.offer_count = offer_count
            self.offer_price = offer_price

        def total_price(self):
            count = max(self.count, 0)
            total_price = 0

            total_price += (count // self.offer_count) * self.offer_price

            count = count % self.offer_count
            total_price += count * self.price

            return total_price


    class cross_offer_item(item):
        def __init__(self, name, price, count, offer_count, cross_item):
            super().__init__(name, price, count)

            self.offer_count = offer_count
            self.cross_item = cross_item

        def cross_offer(self):
            cross_item = items_table[self.cross_item]
            cross_item.count -= (self.count // self.offer_count)

    class group_offer_item(item):
        def __init__(self, name, price, count, offer_count, offer_price, group_name):
            super().__init__(name, price, count)

            self.offer_count = offer_count
            self.offer_price = offer_price

    skus_counter = Counter(skus)

    A = two_level_offer_item(name="A", price=50, count=skus_counter["A"],
                             first_offer_count=5, first_offer_price=200,
                             second_offer_count=3, second_offer_price=130)

    B = one_level_offer_item(name="B", price=30, count=skus_counter["B"],
                             offer_count=2, offer_price=45)

    C = item(name="C", price=20, count=skus_counter["C"])

    D = item(name="D", price=15, count=skus_counter["D"])

    E = cross_offer_item(name="E", price=40, count=skus_counter["E"],
                         offer_count=2, cross_item="B")

    F = one_level_offer_item(name="F", price=10, count=skus_counter["F"],
                             offer_count=3, offer_price=20)

    G = item(name="G", price=20, count=skus_counter["G"])

    H = two_level_offer_item(name="H", price=10, count=skus_counter["H"],
                             first_offer_count=10, first_offer_price=80,
                             second_offer_count=5, second_offer_price=45)

    I = item(name="I", price=35, count=skus_counter["I"])

    J = item(name="J", price=60, count=skus_counter["J"])

    K = one_level_offer_item(name="K", price=70, count=skus_counter["K"],
                             offer_count=2, offer_price=120)

    L = item(name="L", price=90, count=skus_counter["L"])

    M = item(name="M", price=15, count=skus_counter["M"])

    N = cross_offer_item(name="N", price=40, count=skus_counter["N"],
                         offer_count=3, cross_item="M")

    O = item(name="O", price=10, count=skus_counter["O"])

    P = one_level_offer_item(name="P", price=50, count=skus_counter["P"],
                             offer_count=5, offer_price=200)

    Q = one_level_offer_item(name="Q", price=30, count=skus_counter["Q"],
                             offer_count=3, offer_price=80)

    R = cross_offer_item(name="R", price=50, count=skus_counter["R"],
                         offer_count=3, cross_item="Q")

    S = item(name="S", price=30, count=skus_counter["S"])

    T = item(name="T", price=20, count=skus_counter["T"])

    U = one_level_offer_item(name="U", price=40, count=skus_counter["U"],
                             offer_count=4, offer_price=120)

    V = two_level_offer_item(name="V", price=50, count=skus_counter["V"],
                             first_offer_count=3, first_offer_price=130,
                             second_offer_count=2, second_offer_price=90)

    W = item(name="W", price=20, count=skus_counter["W"])

    X = item(name="X", price=90, count=skus_counter["X"])

    Y = item(name="Y", price=10, count=skus_counter["Y"])

    Z = item(name="Z", price=50, count=skus_counter["Z"])

    items_table = { "A": A,
                    "B": B,
                    "C": C,
                    "D": D,
                    "E": E,
                    "F": F,
                    "G": G,
                    "H": H,
                    "I": I,
                    "J": J,
                    "K": K,
                    "L": L,
                    "M": M,
                    "N": N,
                    "O": O,
                    "P": P,
                    "Q": Q,
                    "R": R,
                    "S": S,
                    "T": T,
                    "U": U,
                    "V": V,
                    "W": W,
                    "X": X,
                    "Y": Y,
                    "Z": Z}

    for item, count in skus_counter.items():
        if item not in items_table.keys(): return -1
        items_table[item].cross_offer()

    basket_value = 0
    for item in items_table.values():
        basket_value += item.total_price()

    return basket_value

